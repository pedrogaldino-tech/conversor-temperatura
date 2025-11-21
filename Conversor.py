---

## 4) conversor-temperatura  
*Descrição sugerida:* Conversor de temperatura (C ↔ F) em Python.

*Arquivo:* conversor_temperatura.py  
```python
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Conversor de Temperatura")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    opcao = input("Escolha a opção: ")

    try:
        valor = float(input("Digite o valor da temperatura: "))
    except ValueError:
        print("Valor inválido.")
        return

    if opcao == "1":
        resultado = celsius_para_fahrenheit(valor)
        print(f"{valor}°C equivalem a {resultado:.2f}°F")
    elif opcao == "2":
        resultado = fahrenheit_para_celsius(valor)
        print(f"{valor}°F equivalem a {resultado:.2f}°C")
    else:
        print("Opção inválida.")

if _name_ == "_main_":
    main()
