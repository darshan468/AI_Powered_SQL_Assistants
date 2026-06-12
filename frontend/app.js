const API_BASE = 'http://localhost:8000';
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const schemaContent = document.getElementById('schema-content');

// Load schema on start
async function loadSchema() {
    try {
        const response = await fetch(`${API_BASE}/schema`);
        const data = await response.json();
        
        const lines = data.schema.trim().split('\n');
        schemaContent.innerHTML = '';
        lines.forEach(line => {
            const block = document.createElement('div');
            block.className = 'schema-block';
            block.innerHTML = line.replace('Table:', '<strong>Table:</strong>')
                                  .replace('(', '<code>(').replace(')', ')</code>');
            schemaContent.appendChild(block);
        });
        schemaContent.classList.remove('loading-schema');
    } catch (err) {
        schemaContent.innerHTML = '<div class="error">Failed to load schema. Make sure backend is running.</div>';
    }
}

async function appendMessage(role, content, extra = null) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;
    
    const icon = role === 'bot' ? 'robot' : 'user';
    
    let html = `
        <div class="avatar"><i class="fas fa-${icon}"></i></div>
        <div class="content">
            <p class="${role === 'bot' ? 'typing-text' : ''}">${role === 'bot' ? '' : content}</p>
    `;
    
    msgDiv.innerHTML = html;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const contentP = msgDiv.querySelector('p');

    if (role === 'bot') {
        // Typewriter effect
        await typeText(contentP, content);
        
        if (extra && extra.sql) {
            const sqlDiv = document.createElement('div');
            sqlDiv.className = 'sql-block';
            sqlDiv.textContent = extra.sql;
            msgDiv.querySelector('.content').appendChild(sqlDiv);
        }
        
        if (extra && extra.data && extra.data.length > 0) {
            const tableWrapper = document.createElement('div');
            tableWrapper.innerHTML = renderTable(extra.data);
            msgDiv.querySelector('.content').appendChild(tableWrapper.firstElementChild);
        } else if (extra && extra.data && extra.data.length === 0) {
            const noRes = document.createElement('p');
            noRes.style.color = 'var(--accent)';
            noRes.style.marginTop = '1rem';
            noRes.textContent = 'No results found.';
            msgDiv.querySelector('.content').appendChild(noRes);
        }
    } else {
        // User message, already set
    }
    
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function typeText(element, text) {
    return new Promise(resolve => {
        let i = 0;
        element.classList.add('typing');
        const interval = setInterval(() => {
            element.textContent += text[i];
            i++;
            if (i >= text.length) {
                clearInterval(interval);
                element.classList.remove('typing');
                resolve();
            }
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 10);
    });
}

function renderTable(data) {
    const keys = Object.keys(data[0]);
    let html = `
        <div class="result-table-wrapper">
            <table>
                <thead>
                    <tr>${keys.map(k => `<th>${k}</th>`).join('')}</tr>
                </thead>
                <tbody>
                    ${data.map(row => `
                        <tr>${keys.map(k => `<td>${row[k]}</td>`).join('')}</tr>
                    `).join('')}
                </tbody>
            </table>
        </div>
    `;
    return html;
}

async function handleSendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    userInput.value = '';
    appendMessage('user', query);

    // Create a temporary loading message with premium indicator
    const loadingId = Date.now();
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot';
    loadingDiv.id = `loading-${loadingId}`;
    loadingDiv.innerHTML = `
        <div class="avatar"><i class="fas fa-robot"></i></div>
        <div class="content">
            <div class="typing-indicator">
                <span></span><span></span><span></span>
            </div>
        </div>
    `;
    chatMessages.appendChild(loadingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });
        
        const result = await response.json();
        chatMessages.removeChild(loadingDiv);

        if (result.status === 'success' || result.mode === 'sql' || result.mode === 'text') {
            let messageText = result.message;
            if (!messageText && result.mode === 'sql') {
                messageText = "I've analyzed the database and here is the information:";
            }
            appendMessage('bot', messageText || "I'm not sure how to answer that.", result);
        } else {
            appendMessage('bot', result.message || "An error occurred.", result);
        }
    } catch (err) {
        if (chatMessages.contains(loadingDiv)) {
            chatMessages.removeChild(loadingDiv);
        }
        appendMessage('bot', "Could not connect to the API. Is the server running?");
    }
}


function useSuggestion(text) {
    userInput.value = text;
    handleSendMessage();
}

sendBtn.addEventListener('click', handleSendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleSendMessage();
});

// Init
loadSchema();
window.useSuggestion = useSuggestion;
