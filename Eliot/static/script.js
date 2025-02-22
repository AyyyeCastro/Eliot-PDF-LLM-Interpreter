document.addEventListener('DOMContentLoaded', () => {
    const pdfFileUploader = document.getElementById('pdfFile');
    const modelChoiceSelector = document.getElementById('model-choice');
    const summarizeButton = document.getElementById('send-button');
    const summaryOutputDiv = document.getElementById('summaryOutput');
    const summaryTextSpan = document.getElementById('summaryText');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const chatContainer = document.getElementById('userMessage-container');
    const promptInput = document.getElementById('promptInput');
    const defaultPrompt = document.getElementById('defaultPrompt').value;
    const warningInfo = document.getElementById('warningInfo');
    const getInputBar = document.getElementById('text-input-bar');
    const getTaskTypeContainer = document.getElementById('task-type-container');
    const getinstructionParentContainer = document.getElementById('instruction-parent-container');
    const getModelChoiceContainer = document.getElementById('model-choice-container');
 
 
    let uploadedFile = null;
    let attachmentMessage = null;
 
    function updatePromptInput() {
       const selectedModel = modelChoiceSelector.value;
       if (selectedModel === "11" || selectedModel === "12") {
          promptInput.removeAttribute('readonly');
          promptInput.value = '';
          promptInput.placeholder = "Enter your custom prompt here...";
          warningInfo.classList.remove('flashWarning');
          promptInput.classList.remove('readOnlyInput');
          promptInput.removeEventListener('click', readOnlyClickHandler);
          getInputBar.classList.add('col-12');
          getInputBar.classList.remove('col-auto');
 
          getModelChoiceContainer.classList.remove('col-lg-6');
          getinstructionParentContainer.classList.remove('col-lg-6');
          getModelChoiceContainer.classList.remove('col-lg-4');
          getTaskTypeContainer.classList.remove('hideTaskTypeContainer');
 
 
          getinstructionParentContainer.classList.add('col-lg-4');
          getModelChoiceContainer.classList.add('col-lg-4');
          getTaskTypeContainer.classList.add('col-lg-4');
          getTaskTypeContainer.classList.add('col-md-12');
 
          getInputBar.classList.add('animateOpen');
          getInputBar.classList.remove('animateClosed');
 
 
       } else {
          promptInput.setAttribute('readonly', true);
          promptInput.value = defaultPrompt;
          promptInput.placeholder = '';
          promptInput.classList.add('readOnlyInput');
          warningInfo.classList.add('flashWarning');
          getInputBar.classList.add('col-auto');
          getInputBar.classList.remove('col-12');
 
          getinstructionParentContainer.classList.remove('col-lg-8');
          modelChoiceSelector.classList.remove('col-lg-4');
          getTaskTypeContainer.classList.remove('col-lg-3');
          getTaskTypeContainer.classList.remove('col-md-12');
 
          getinstructionParentContainer.classList.add('col-lg-6');
          getModelChoiceContainer.classList.add('col-lg-6');
          getTaskTypeContainer.classList.add('hideTaskTypeContainer');
 
 
          getInputBar.classList.remove('animateOpen');
          getInputBar.classList.add('animateClosed');
 
 
          if (promptInput.classList.contains('readOnlyInput')) {
             promptInput.addEventListener('click', readOnlyClickHandler);
          }
       }
    }
 
    function readOnlyClickHandler() {
       alert("Summarizer models can not use custom prompts. They will use the best one for summarizing text by default.");
    }
 
    updatePromptInput();
    modelChoiceSelector.addEventListener('change', updatePromptInput);
 
    pdfFileUploader.addEventListener('change', function () {
       if (this.files && this.files[0]) {
          uploadedFile = this.files[0];
       }
    });
 
    summarizeButton.addEventListener('click', async () => {
       const pdfFile = uploadedFile;
       const modelChoice = modelChoiceSelector.value;
       const userPrompt = promptInput.value;
       const taskType = document.getElementById('task-type').value;
 
       if (!pdfFile) {
          alert("Please select a PDF file to summarize.");
          return;
       }
 
       const fileName = pdfFile.name;
 
 
       if (attachmentMessage && chatContainer.contains(attachmentMessage)) {
          chatContainer.removeChild(attachmentMessage);
       }
 
 
       attachmentMessage = document.createElement('div');
       attachmentMessage.classList.add('message', 'user-message');
       attachmentMessage.innerHTML = `
             <div><strong>Attached file:</strong> ${fileName}</div>
             <div> ${userPrompt}</div>
         `;
       chatContainer.appendChild(attachmentMessage);
 
 
       requestAnimationFrame(() => {
          if (chatContainer.firstChild && chatContainer.firstChild.classList.contains('bot-message')) {
             chatContainer.removeChild(chatContainer.firstChild);
          }
       });
 
 
       summaryTextSpan.textContent = "Summarizing";
       summaryOutputDiv.style.display = 'flex';
       loadingSpinner.style.display = 'inline-block';
 
       const formData = new FormData();
       formData.append('pdfFile', pdfFile);
       formData.append('modelChoice', modelChoice);
       formData.append('prompt', userPrompt);
       formData.append('taskType', taskType);
 
       try {
          const response = await fetch('/process', {
             method: 'POST',
             body: formData,
          });
 
          if (!response.ok) {
             const errorData = await response.json();
             summaryTextSpan.textContent = `Error: ${errorData.error || response.statusText}`;
             loadingSpinner.style.display = 'none';
             return;
          }
 
          const data = await response.json();
          summaryTextSpan.textContent = data.result;
          loadingSpinner.style.display = 'none';
 
          requestAnimationFrame(() => {
             summaryTextSpan.style.animation = 'glitch 1.0s forwards';
             loadingSpinner.style.display = 'none';
          });
 
       } catch (error) {
          console.error("Error:", error);
          summaryTextSpan.textContent = "An unexpected error occurred.";
          loadingSpinner.style.display = 'none';
       }
    });
 
    const sidebar = document.getElementById("sidebar-container");
 
    function toggleSidebar() {
       sidebar.classList.toggle("active");
    }
    sidebar.addEventListener("mouseover", toggleSidebar);
    sidebar.addEventListener("mouseleave", toggleSidebar);
 
 
 });