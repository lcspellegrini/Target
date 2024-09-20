let a = 0, b = 1;
let fibonacci = 0;
let lista = [1];
let n = document.getElementById("inputText100").value;
function verificar() {
    for (let i = 0; i < 10; i++) {
        fibonacci = a + b;
        lista.push(fibonacci);
        a = b;
        b = fibonacci;
        console.log(lista);
        
    }
}
verificar ();
lista.includes(n) ? console.log("O número", n, "faz parte da sequencia de Fibonacci") : console.log("O número ", n, "não faz parte da sequencia de Fibonacci");
