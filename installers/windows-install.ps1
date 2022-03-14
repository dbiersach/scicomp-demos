Set-Location $HOME
conda update -y -n base conda
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -y -n scicomp-demos python=3.9
conda activate scicomp-demos
conda install -y matplotlib sympy scipy scikit-learn
conda install -y pandas pandasql docutils pandocfilters
conda install -y numexpr h5py traitsui zipp pathspec openpyxl
conda install -y pylint autopep8 black
conda install -y websockets requests pyserial
conda install -y ipython ipykernel ipympl
conda install -y nodejs
conda install -y jupyterlab jupyterlab_code_formatter
conda install -y numba
conda update -y --all
