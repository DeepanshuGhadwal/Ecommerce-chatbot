import React, { useState } from 'react';
import axios from 'axios';

const ChatbotPage = () => {
  const [input, setInput] = useState('');
  const [responses, setResponses] = useState([]);

  const handleSend = async () => {
    const res = await axios.post('http://localhost:5000/chat', { query: input });
    setResponses([...responses, { query: input, response: res.data }]);
    setInput('');
  };

  return (
    <div className="p-4">
      <h1 className="text-xl mb-4 font-bold">E-commerce Chatbot</h1>
      <div className="mb-4">
        <input
          className="border p-2 w-1/2"
          placeholder="Ask about a product..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="ml-2 px-4 py-2 bg-blue-500 text-white" onClick={handleSend}>
          Send
        </button>
      </div>
      <div>
        {responses.map((r, index) => (
          <div key={index} className="mb-4">
            <p><strong>You:</strong> {r.query}</p>
            <p><strong>Bot:</strong> {r.response.message}</p>
            <div className="grid grid-cols-2 gap-4 mt-2">
              {r.response.products.map(p => (
                <div key={p.id} className="border p-2">
                  <img src={p.image_url} alt={p.name} className="w-full h-24 object-cover" />
                  <p className="font-semibold">{p.name}</p>
                  <p>₹{p.price}</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatbotPage;
