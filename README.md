# Image Generator

## Descrição

Este componente gera uma imagem a partir de um texto fornecido e retorna a imagem como uma string base64. Ele utiliza o modelo Stable Diffusion da Hugging Face para a geração de imagens.

## Pré-requisitos

1. **Verificar suporte a GPU: Para verificar se a sua máquina possui suporte a GPU, execute:**

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

<br>

2. **Instalação do PyTorch**

- Se a sua máquina tiver uma GPU, instale o PyTorch com suporte CUDA:

```bash
pip install torch torchvision torchaudio --index-url <https://download.pytorch.org/whl/cu118>
```

- Se não tiver uma GPU, instale o PyTorch para CPU:

```bash
pip install torch torchvision torchaudio
```

<br>

3. **Instalação das dependências do Diffusers: Instale as bibliotecas necessárias**:

```bash
pip install diffusers transformers scipy ftfy accelerate
pip install huggingface-hub
```

<br>

4. **Configuração do Hugging Face**:

- Crie uma conta no Hugging Face.

- Faça login no Hugging Face usando o token de usuário:

```bash
huggingface-cli login {seu-token}
```

<br>

5. **Baixar o modelo Stable Diffusion**:

```bash
huggingface-cli download CompVis/stable-diffusion-v1-4 --local-dir ./stable_diffusion_model
```

<br>

6. **Atualização do sistema (opcional): Para garantir que tudo esteja atualizado, você pode executar**:

```bash
sudo apt update && sudo apt upgrade
```

<br>

## Entradas

| Nome | Tipo | Descrição | Obrigatório |
|------|------|-----------|-------------|
| prompt | String | Texto que será utilizado para gerar a imagem. | Sim |
| width | Int | Largura da imagem gerada (em pixels). Valor padrão é 512. | Sim |
| height | Int | Altura da imagem gerada (em pixels). Valor padrão é 512. | Sim |

## Saídas

| Nome | Tipo | Descrição |
|------|------|-----------|
| base64_image | String | A imagem gerada representada como uma string base64. |
