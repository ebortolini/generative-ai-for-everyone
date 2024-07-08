# Setup Virtual Environment
You can find the complete references [here](https://platform.openai.com/docs/quickstart)

All the instructions are Windows based

## Create virtual environment

``` powershell
python -m venv openai-env
```

## Activate

``` powershell
.\openai-env\Scripts\activate
```

## Install openAI
``` powershell
pip install --upgrade openai
```

## Set enviroment variable
``` powershell
$env:OPENAI_API_KEY = 'MyTestResourceGroup'
```