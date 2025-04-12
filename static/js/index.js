let upiField;
let errorElement;

let invalidUPI = () => alert("Invalid UPI");

window.onload = () => {
    let html5QrcodeScanner = new Html5QrcodeScanner("qr-scanner", { fps: 15, qrbox: 250 });
    html5QrcodeScanner.render(onScanSuccess);

    let upiForm = document.querySelector("#upi-form");
    upiField = document.querySelector("#upi-id");
    errorElement = document.querySelector("#error-msg");

    upiField.addEventListener("blur", validateUPI);
    upiField.addEventListener("focus", removeValidation);
    upiForm.addEventListener("submit", (e) => validateForm(e));
};

function onScanSuccess(decodedText) {
    let queryString = decodedText.split('?')[1];
    if (queryString) {
        let params = new URLSearchParams(queryString);
        let upiId = params.get("pa");
        if (upiId) {
            let upiField = document.getElementById("upi-id");
            upiField.value = upiId;
            validateUPI();
        } else invalidUPI();
    } else invalidUPI();
}

function validateUPI() {
    let upiReg = /^[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.\-_]+$/;
    let isValid = upiReg.test(upiField.value.trim());

    upiField.classList.toggle("error", !isValid);
    errorElement.classList.toggle("d-none", isValid);

    return isValid;
}

function removeValidation() {
    upiField.classList.remove("error");
    errorElement.classList.add("d-none");
}

function validateForm(form) {
    let isValid = validateUPI();
    if (!isValid) {
        form.preventDefault();
    }
}