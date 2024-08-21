from django.contrib.auth.models import BaseUserManager

class AlunoManager(BaseUserManager):
    # Método para criar um usuário comum
    def create_user(self, matricula, password, **extra_fields):
        if not matricula:
            raise ValueError('O campo matrícula é obrigatório.')
        # Cria um usuário com os campos fornecidos e define a senha
        user = self.model(
            matricula=matricula,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    # Método para criar um superusuário
    def create_superuser(self, matricula, password, **extra_fields):
        # Define is_staff e is_superuser como True por padrão
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Verifica se o superusuário possui as permissões necessárias
        if not extra_fields.get('is_staff'):
            raise ValueError('superuser must have is_staff = True')
        if not extra_fields.get('is_staff'):
            raise ValueError('superuser must have is_superuser = True')
        
        # Chama o método create_user para criar o superusuário
        return self.create_user(matricula, password, **extra_fields)

    # Método para buscar um usuário pelo atributo 'matricula'
    def get_by_natural_key(self, matricula):
        return self.get(matricula=matricula)
