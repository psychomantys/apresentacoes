# Metodo antigo
mpirun -np 4 ./executavel arg1 arg2 ... argN

# Novo metodo
qsub -l nodes=4:ppn=8 <<<"mpirun ./executavel arg1 arg2 ... argN"

# Saidas do programa
ls STDIN.*
STDIN.o19	STDIN.e19
