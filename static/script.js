// HealthMate Chatbot JavaScript

// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const voiceBtn = document.getElementById('voiceBtn');
const language = document.getElementById('language');
const quickSuggestionsContainer = document.getElementById('quickSuggestions');
const welcomeScreen = document.getElementById('welcomeScreen');

// State
let isTyping = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadQuickSuggestions();
    showWelcomeMessage();
    
    // Event listeners
    sendBtn.addEventListener('click', handleSendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    });
    voiceBtn.addEventListener('click', startVoiceInput);
    
    // Focus input on load
    userInput.focus();
});

// Show welcome message
function showWelcomeMessage() {
    const tip = "💡 Try asking me about symptoms, nutrition, exercise, or vaccinations!";
    setTimeout(() => {
        addMessage('bot', `Hello! 👋 I'm your HealthMate assistant. I can help you with health information, symptoms, nutrition, exercise, and more. How can I assist you today?\n\n${tip}`);
        hideWelcomeScreen();
    }, 500);
}

// Hide welcome screen
function hideWelcomeScreen() {
    if (welcomeScreen) {
        welcomeScreen.classList.add('fadeOut');
        setTimeout(() => {
            welcomeScreen.style.display = 'none';
        }, 300);
    }
}

// Load quick suggestions
async function loadQuickSuggestions() {
    const suggestions = [
        "What to do for fever?",
        "Healthy diet tips",
        "Exercise recommendations",
        "Stress management",
        "Child vaccination schedule",
        "Sleep better"
    ];
    
    quickSuggestionsContainer.innerHTML = '';
    suggestions.forEach(suggestion => {
        const chip = document.createElement('button');
        chip.className = 'suggestion-chip';
        chip.textContent = suggestion;
        chip.onclick = () => {
            userInput.value = suggestion;
            handleSendMessage();
        };
        quickSuggestionsContainer.appendChild(chip);
    });
}

// Handle send message
async function handleSendMessage() {
    const text = userInput.value.trim();
    if (text === '' || isTyping) return;
    
    // Hide welcome screen if visible
    hideWelcomeScreen();
    
    // Add user message
    addMessage('user', text);
    userInput.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    try {
        // Send to backend
        const response = await fetch('/api/message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                text: text, 
                language: language.value 
            })
        });
        
        const data = await response.json();
        
        // Simulate typing delay
        setTimeout(() => {
            hideTypingIndicator();
            addMessage('bot', data.response);
        }, 800);
        
    } catch (error) {
        hideTypingIndicator();
        addMessage('bot', 'Sorry, I encountered an error. Please try again.');
        console.error('Error:', error);
    }
}

// Add message to chat
function addMessage(sender, text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = sender === 'user' ? '👤' : '🏥';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Format text with line breaks
    const formattedText = text.replace(/\n/g, '<br>');
    contentDiv.innerHTML = formattedText;
    
    // Add timestamp
    const time = document.createElement('div');
    time.className = 'message-time';
    time.textContent = getCurrentTime();
    contentDiv.appendChild(time);
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    scrollToBottom();
}

// Show typing indicator
function showTypingIndicator() {
    isTyping = true;
    
    const typingDiv = document.createElement('div');
    typingDiv.id = 'typingIndicator';
    typingDiv.className = 'message bot';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = '🏥';
    
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    
    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.className = 'typing-dot';
        indicator.appendChild(dot);
    }
    
    typingDiv.appendChild(avatar);
    typingDiv.appendChild(indicator);
    chatContainer.appendChild(typingDiv);
    
    scrollToBottom();
}

// Hide typing indicator
function hideTypingIndicator() {
    isTyping = false;
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

// Voice input
function startVoiceInput() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Voice recognition is not supported in this browser. Please try Chrome or Edge.');
        return;
    }
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.lang = language.value === 'hindi' ? 'hi-IN' : 'en-US';
    recognition.continuous = false;
    recognition.interimResults = false;
    
    // Visual feedback
    voiceBtn.style.background = 'var(--teal-gradient)';
    voiceBtn.style.color = 'white';
    
    recognition.start();
    
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        voiceBtn.style.background = '';
        voiceBtn.style.color = '';
    };
    
    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        voiceBtn.style.background = '';
        voiceBtn.style.color = '';
        
        if (event.error === 'no-speech') {
            alert('No speech detected. Please try again.');
        } else if (event.error === 'not-allowed') {
            alert('Microphone access denied. Please allow microphone access in your browser settings.');
        } else {
            alert('Voice recognition error. Please try again.');
        }
    };
    
    recognition.onend = () => {
        voiceBtn.style.background = '';
        voiceBtn.style.color = '';
    };
}

// Scroll to bottom
function scrollToBottom() {
    setTimeout(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 100);
}

// Get current time
function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

// Auto-resize input
userInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 120) + 'px';
});
