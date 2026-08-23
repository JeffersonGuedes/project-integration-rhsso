# arquivo: auth.py (crie este arquivo)
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class KeycloakOIDCBackend(OIDCAuthenticationBackend):
    
    def create_user(self, claims):
        """Chamado quando um usuário loga pela primeira vez."""
        user = super().create_user(claims)
        
        # Opcional: já puxa Nome e Sobrenome do Keycloak
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        
        # Verifica a role e atualiza as permissões
        self._update_admin_privileges(user, claims)
        
        return user

    def update_user(self, user, claims):
        """Chamado em todos os logins subsequentes do usuário."""
        # Mantém as informações sincronizadas com o Keycloak
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        
        # Atualiza permissões a cada login
        self._update_admin_privileges(user, claims)
        
        return user

    def _update_admin_privileges(self, user, claims):
        """Regra de negócio: se tiver a role no Keycloak, vira admin no Django."""
        # A estrutura de roles no userinfo do Keycloak geralmente vem assim:
        # "realm_access": {"roles": ["django_admin", "outra_role"]}
        realm_access = claims.get('realm_access', {})
        roles = realm_access.get('roles', [])
        
        has_admin_role = 'django_admin' in roles

        # Só faz a query de UPDATE no banco se houver mudança
        if user.is_staff != has_admin_role or user.is_superuser != has_admin_role:
            user.is_staff = has_admin_role
            user.is_superuser = has_admin_role
            user.save()