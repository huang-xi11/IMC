async function inviaDati() {
    const nome = document.getElementById("nome").value;
    const peso = document.getElementById("peso").value;
    const altezza = document.getElementById("altezza").value;

    const risposta = await fetch("/IMC", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome: nome,
            peso: peso,
            altezza: altezza
        })
    });

    const dati = await risposta.json();

    document.getElementById("risultato").innerText =
        "IMC: " + dati.imc;
}