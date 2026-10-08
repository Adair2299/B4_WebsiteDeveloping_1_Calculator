document.getElementById("calculate").addEventListener("click", async function () {
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;

    let response = await fetch(`/calculate?a=${a}&b=${b}`);
    let data = await response.json();

    document.getElementById("result").innerText = "Result: " + data.result;
});