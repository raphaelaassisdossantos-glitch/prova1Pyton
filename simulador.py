#-- Pergunta incial --
continuar = "sim"

while continuar == "sim":
     continuar = input("você deseja continuar jogando ? (sim/não): ")

     if continuar == "sim":
        print("voce ainda esta no jogo")
     elif continuar == "não":
        print("Gamer over")
     else:
        print("opção invalido. digite sim ou não ")
        continuar = "sim"
