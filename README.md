# Lattice

$BASE_DIR = $HOME/Atoms_Project
mkdir $BASE_DIR

cd $BASE_DIR

brew install python3
Brew install git
pip3 install virtualenv
virtualenv -p python3 atoms-env
source atoms-env/bin/activate

pip install numpy
pip install sklearn

git clone https://github.com/atorefrank/Lattice.git

cd lattice/
python ase_chrystals.py