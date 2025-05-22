function addOption() {
    const optionsContainer = document.getElementById('optionsContainer');
    const newOptionItem = `
        <li class="option-item">
                <div>
                    <input type="text" name="choice" placeholder="Enter choice title" class="choice-text-field__input" required/>
                    <button type="button" onclick="removeOption(this)" class="btn btn-danger">Remove</button>
                </div>
            </li>
    `;
    optionsContainer.insertAdjacentHTML("beforeend", newOptionItem);
}

function removeOption(button) {
    const optionsContainer = document.getElementById('optionsContainer');
    if (optionsContainer.childElementCount <= 2) return;
    button.closest('.option-item').remove();
}

document.querySelector('#pollForm').onsubmit = function(event) {
    event.preventDefault();
};