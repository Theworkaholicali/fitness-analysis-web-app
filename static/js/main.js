const formScreen = document.getElementById("form-screen")
const resultScreen = document.getElementById("result-screen")

document.getElementById("fitnessForm").addEventListener("submit", async (e) => {
    e.preventDefault()

    const formData = Object.fromEntries(new FormData(e.target))

    const res = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    })

    const data = await res.json()
    showResults(data)
})

function showResults(data) {
    const score = data.metrics.fitness_score
    let color

    if (score >= 75) color = "#00ff88"
    else if (score >= 55) color = "#ffd000"
    else color = "#ff4d4d"

    
    document.getElementById("score-ring").style.color = color
    animateScoreRing(score, color)

    document.getElementById("metrics").innerHTML = `
        <h3 style="color:${color}">BMI: ${data.metrics.bmi}</h3>
        <h3 style="color:${color}">Calories: ${data.metrics.daily_calories}</h3>
    `

    document.getElementById("suggestions").innerHTML =
        `<ul>${data.insights.map(t => `<li style="color:${color}">${t}</li>`).join("")}</ul>`

    renderBMIBar(data.metrics.bmi, color)
    renderPopulationComparison(data.metrics.bmi)

    formScreen.classList.remove("active")
    resultScreen.classList.add("active")
}

function renderBMIBar(bmi, color) {
    const indicator = document.getElementById("bmi-indicator")
    const position = Math.min(Math.max((bmi / 40) * 100, 0), 100)

    indicator.style.left = `${position}%`
    indicator.style.background = color
}

function renderPopulationComparison(bmi) {
    let msg
    if (bmi < 18.5) msg = "Below 15% of population"
    else if (bmi < 25) msg = "Healthier than ~60% of population"
    else msg = "Higher BMI than ~70% of population"

    document.getElementById("population").innerHTML =
        `<p>${msg}</p>`
}

document.getElementById("backBtn").onclick = () => {
    resultScreen.classList.remove("active")
    formScreen.classList.add("active")
}

document.getElementById("resetBtn").onclick = () => {
    location.reload()
}

function animateScoreRing(targetScore, color) {
    const ring = document.getElementById("score-ring")
    let current = 0

    const interval = setInterval(() => {
        current++

        ring.style.background =
            `conic-gradient(${color} ${current * 3.6}deg, #222 0deg)`
        ring.style.color = "#000"
        ring.innerText = current

        if (current >= targetScore) {
            clearInterval(interval)
        }
    }, 20)
}

