document.getElementById("date").addEventListener("input", async (e) => {
    const date = e.target.value;
    if (date) {
        const response = await fetch(`/calculate-age?date=${date}`);
        const data = await response.json();
        if (data.age !== undefined) {
            document.getElementById("age-display").textContent = `This person is ${data.age} years old`;
        } else {
            document.getElementById("age-display").textContent = data.error;
        }

        e.target.value = "";
    } else {
        document.getElementById("age-display").textContent = "Enter date of birth to see the age";
    }
});
