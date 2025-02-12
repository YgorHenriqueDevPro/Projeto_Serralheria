from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Somente usuários autenticados
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CadastroForm
from .models import Cliente

# Cadastro de Usuário
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])  # Criptografa a senha
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'clientes/cadastro.html', {'form': form})

# Login de usuário
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('cliente:listar_clientes')  # Redireciona para a página de listagem de clientes
        else:
            # Verifica se o usuário existe antes de exibir a mensagem de erro
            if not User.objects.filter(username=username).exists():
                messages.error(request, "Usuário não cadastrado, por favor realize seu cadastro e tente novamente.")
            else:
                messages.error(request, "Login ou senha inválidos. Tente novamente.")
    
    return render(request, 'clientes/login.html')

# Listar Clientes (Somente usuários autenticados)
@login_required
def listar_clientes(request):
    # Verifica se há um termo de pesquisa no GET
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Filtra os clientes pelo nome, caso haja um termo de pesquisa
        clientes = Cliente.objects.filter(nome__icontains=search_query)
    else:
        # Caso não haja pesquisa, retorna todos os clientes
        clientes = Cliente.objects.all()

    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

# Adicionar Cliente
@login_required
def adicionar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        endereco = request.POST.get('endereco')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        # Cria o cliente e salva no banco
        Cliente.objects.create(
            nome=nome,
            cpf_cnpj=cpf_cnpj,
            endereco=endereco,
            celular=celular,
            email=email,
            telefone=telefone
        )
        messages.success(request, "Cliente adicionado com sucesso!")
        return redirect('cliente:listar_clientes')
    
    return render(request, 'clientes/adicionar_cliente.html')

# Editar Cliente
@login_required
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.cpf_cnpj = request.POST.get('cpf_cnpj')
        cliente.endereco = request.POST.get('endereco')
        cliente.celular = request.POST.get('celular')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.save()
        messages.success(request, "Cliente editado com sucesso!")
        return redirect('cliente:listar_clientes')
    
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

# Excluir Cliente
@login_required
def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
        return redirect('cliente:listar_clientes')
    
    return render(request, 'clientes/excluir_cliente.html', {'cliente': cliente})
