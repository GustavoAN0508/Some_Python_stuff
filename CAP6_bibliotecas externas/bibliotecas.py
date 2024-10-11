import platform

print("distribuição do sistema operacional:", platform.platform())
print("nome do sistema operacional:", platform.system())
print("versão do sistema operacional:", platform.release())
print("arquitetura:", platform.architecture())
print("nome do computador:", platform.node())
print("tipo de maquina:", platform.machine())
print("processador", platform.processor())
print("versão do python", platform.python_version())