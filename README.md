# stedmund-summer-python-workshop
All material for the python workshop at St Edmund College, Cambridge, for a summer programme 3rd - 16th Aug

## Contact
Cheng-Yu Huang "Kou" (cyh37@cam.ac.uk)

## Slides
Slides used in this workshop can be found here: [LINK](LINK_HERE)

## Pre-requirement of the workshop

Please prepare the following before the workshop:

- Please install [Miniconda](https://www.anaconda.com/download/success#miniconda) on your laptop. We will use miniconda to create an environment for coding (i.e. venv)

- Follow the **Creating a Python Environment for the workshop** workflow below for the setup.

- Please install [Github desktop](https://desktop.github.com/download/) on your laptop. This will help with collaborative coding

- install [Visual Studio Code](https://code.visualstudio.com/download). We will use this as the coding interface (IDE)

## Creating a Python Environment for the workshop

1. Open Anaconda Prompt. 
    - if you are using a **Windows OS machine**, look for **anaconda prompt (miniconda)** in **Start (開始工具列)**. For details, check the step 1 [here](https://kiwi-half.medium.com/python-anaconda-%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E5%BB%BA%E7%BD%AEanaconda-prompt-virtual-environment-9e93c5789627)
    - if you are using a **Mac OS machine**, look for **terminal (終端機)**. For detailed instruction, check [here](https://support.apple.com/zh-tw/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)


2. With the Anaconda prompt, create a virtual environment with the name “sted-workshop-venv”

    ```powershell
    conda create --name sted-workshop-venv python=3.11
    ```

3. Then activate the environment

    ```powershell
    conda activate sted-workshop-venv
    ```
    You should notice that the start of the command line is now `(sted-workshop-venv)`
    
4. Install all the basic python packages with

    ```powershell
    conda install numpy matplotlib scipy scikit-image ipywidgets jupyter jupyterlab pandas scikit-learn seaborn
    ```

P.S. other useful conda command:
`conda env list` to list all available environment

## Other resources
- Other conda command: https://docs.conda.io/projects/conda/en/4.6.0/user-guide/tasks/manage-environments.html