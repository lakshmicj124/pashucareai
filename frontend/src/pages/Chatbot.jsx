import React, { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import { useLanguage } from "../context/LanguageContext";
import api, { API_BASE_URL } from "../services/api";
import { 
  Bot, Send, Volume2, VolumeX, Trash2, HelpCircle, Activity, 
  Sparkles, User, AlertCircle, Paperclip, Image as ImageIcon, X,
  MessageSquare, Plus, Menu, Globe, MapPin
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const Chatbot = () => {
  const { t, language, setLanguage } = useLanguage();
  
  // Local translations to ensure clean unicode rendering
  const translationsLocal = {
    en: {
      quickQuestions: "Quick Suggestions",
      chat: "PashuCare AI Chat",
      clearChat: "Clear Chat",
      chatPlaceholder: "Ask about symptoms, feed, or animal care...",
      listen: "Listen",
      stop: "Stop",
      assistantGreeting: "Hello! I am your PashuCare AI Assistant. Ask me anything about livestock health, animal diseases, symptoms, prevention, or feed management. You can also upload a photo of a sick animal for AI diagnosis.",
      noSessions: "No previous chats",
      newChat: "New Chat",
      history: "Chat History",
      imageAttached: "Image Attached",
      readyDiagnosis: "Ready for diagnosis",
      animalType: "Animal Type:",
      diagnosing: "Diagnosing...",
      selectLanguage: "Language:",
      nearbyVetsBtn: "Find Nearby Veterinary Hospitals"
    },
    hi: {
      quickQuestions: "त्वरित सुझाव",
      chat: "पशुकेयर एआई चैट",
      clearChat: "चैट साफ़ करें",
      chatPlaceholder: "लक्षण, चारा, या पशु स्वास्थ्य के बारे में पूछें...",
      listen: "सुनें",
      stop: "रोकें",
      assistantGreeting: "नमस्ते! मैं आपका पशुकेयर एआई सहायक हूँ। मवेशियों के स्वास्थ्य, रोगों, रोकथाम या चारा प्रबंधन के बारे में कुछ भी पूछें। आप निदान के लिए बीमार पशु की तस्वीर भी अपलोड कर सकते हैं।",
      noSessions: "कोई पिछला चैट नहीं",
      newChat: "नया चैट",
      history: "चैट इतिहास",
      imageAttached: "छवि संलग्न है",
      readyDiagnosis: "निदान के लिए तैयार",
      animalType: "पशु का प्रकार:",
      diagnosing: "निदान हो रहा है...",
      selectLanguage: "भाषा:",
      nearbyVetsBtn: "नज़दीकी पशु चिकित्सालय खोजें"
    },
    kn: {
      quickQuestions: "ತ್ವರಿತ ಸಲಹೆಗಳು",
      chat: "ಪಶುಕೇರ್ ಎಐ ಚಾಟ್",
      clearChat: "ಚಾಟ್ ತೆರವುಗೊಳಿಸಿ",
      chatPlaceholder: "ರೋಗಲಕ್ಷಣಗಳು, ಮೇವು ಅಥವಾ ಪ್ರಾಣಿಗಳ ಕಾಳಜಿಯ ಬಗ್ಗೆ ಕೇಳಿ...",
      listen: "ಕೇಳಿ",
      stop: "ನಿಲ್ಲಿಸಿ",
      assistantGreeting: "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಪಶುಕೇರ್ ಎಐ ಸಹಾಯಕ. ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ, ರೋಗಗಳು, ತಡೆಗಟ್ಟುವಿಕೆ ಅಥವಾ ಮೇವು ನಿರ್ವಹಣೆ ಬಗ್ಗೆ ಕೇಳಿ. ರೋಗಪತ್ತೆಗಾಗಿ ಪ್ರಾಣಿಯ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಬಹುದು.",
      noSessions: "ಯಾವುದೇ ಚಾಟ್ ಇತಿಹಾಸವಿಲ್ಲ",
      newChat: "ಹೊಸ ಚಾಟ್",
      history: "ಚಾಟ್ ಇತಿಹಾಸ",
      imageAttached: "ಚಿತ್ರವನ್ನು ಲಗತ್ತಿಸಲಾಗಿದೆ",
      readyDiagnosis: "ರೋಗಪತ್ತೆಗೆ ಸಿದ್ಧವಾಗಿದೆ",
      animalType: "ಪ್ರಾಣಿ ಪ್ರಕಾರ:",
      diagnosing: "ರೋಗಪತ್ತೆ ಮಾಡಲಾಗುತ್ತಿದೆ...",
      selectLanguage: "ಭಾಷೆ:",
      nearbyVetsBtn: "ಹತ್ತಿರದ ಪಶುವೈದ್ಯಕೀಯ ಆಸ್ಪತ್ರೆಗಳನ್ನು ಹುಡುಕಿ"
    }
  };

  const localT = translationsLocal[language] || translationsLocal["en"];

  const quickQuestions = {
    en: [
      "What are the symptoms of Lumpy Skin?",
      "How to prevent Mastitis in dairy cows?",
      "What causes PPR in goats?",
      "Best feed recommendations for goats",
      "Timely vaccine schedule for cattle",
    ],
    hi: [
      "लम्पी त्वचा रोग के लक्षण क्या हैं?",
      "दुधारू गायों में थनैला रोग से कैसे बचाएं?",
      "बकरियों में पीपीआर रोग का क्या कारण है?",
      "बकरियों के लिए सर्वोत्तम चारा क्या है?",
      "मवेशियों के लिए उचित टीकाकरण समय सारणी क्या है?"
    ],
    kn: [
      "ಲಂಪಿ ಚರ್ಮ ರೋಗದ ಲಕ್ಷಣಗಳು ಯಾವುವು?",
      "ಹಸುಗಳಲ್ಲಿ ಕೆಚ್ಚಲು ಬಾತು ರೋಗ ತಡೆಯುವುದು ಹೇಗೆ?",
      "ಆಡುಗಳಲ್ಲಿ ಪಿಪಿಆರ್ ರೋಗಕ್ಕೆ ಕಾರಣವೇನು?",
      "ಆಡುಗಳಿಗೆ ಅತ್ಯುತ್ತಮ ಮೇವಿನ ಶಿಫಾರಸುಗಳು ಯಾವುವು?",
      "ಜಾನುವಾರುಗಳಿಗೆ ಲಸಿಕೆ ಹಾಕುವ ಸರಿಯಾದ ವೇಳಾಪಟ್ಟಿ ಏನು?"
    ],
  };

  const [sessions, setSessions] = useState([]);
  const [activeSessionId, setActiveSessionId] = useState(null);
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: localT.assistantGreeting,
    },
  ]);
  
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [speakingId, setSpeakingId] = useState(null);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);

  // Image Upload States
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [imageAnimal, setImageAnimal] = useState("Cow");

  const messagesEndRef = useRef(null);
  const fileInputRef = useRef(null);

  // Fetch sessions on component mount
  useEffect(() => {
    fetchSessions();
  }, []);

  // Update welcome greeting when language changes (only if no active session or messages are just the initial welcome message)
  useEffect(() => {
    if (!activeSessionId && messages.length === 1 && messages[0].role === "assistant") {
      setMessages([
        {
          role: "assistant",
          text: localT.assistantGreeting,
        },
      ]);
    }
  }, [language]);

  // Scroll to bottom when messages update
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  // Clean up speech synthesis when component unmounts
  useEffect(() => {
    return () => {
      if ("speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  const fetchSessions = async () => {
    try {
      const res = await api.get("/api/chat/sessions");
      setSessions(res.data);
    } catch (err) {
      console.error("Failed to fetch sessions", err);
    }
  };

  const selectSession = async (sessionId) => {
    setActiveSessionId(sessionId);
    setLoading(true);
    setError("");
    setMobileSidebarOpen(false);
    
    // Stop any ongoing speech
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    setSpeakingId(null);

    try {
      const res = await api.get(`/api/chat/sessions/${sessionId}/messages`);
      if (res.data && res.data.length > 0) {
        setMessages(res.data.map(m => ({
          role: m.role,
          text: m.text,
          imageUrl: m.imageUrl || null
        })));
      } else {
        setMessages([
          {
            role: "assistant",
            text: localT.assistantGreeting,
          },
        ]);
      }
    } catch (err) {
      console.error("Failed to fetch messages for session", err);
      setError("Could not load chat messages.");
    } finally {
      setLoading(false);
    }
  };

  const deleteSession = async (sessionId, e) => {
    e.stopPropagation();
    try {
      await api.delete(`/api/chat/sessions/${sessionId}`);
      setSessions(prev => prev.filter(s => s.id !== sessionId));
      if (activeSessionId === sessionId) {
        setActiveSessionId(null);
        setMessages([
          {
            role: "assistant",
            text: localT.assistantGreeting,
          },
        ]);
      }
    } catch (err) {
      console.error("Failed to delete session", err);
      setError("Could not delete chat session.");
    }
  };

  const startNewChat = () => {
    setActiveSessionId(null);
    setMessages([
      {
        role: "assistant",
        text: localT.assistantGreeting,
      },
    ]);
    setMobileSidebarOpen(false);
    setError("");
    removeSelectedImage();
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    setSpeakingId(null);
  };

  const handleImageChange = (e) => {
    setError("");
    const file = e.target.files[0];
    if (file) {
      if (file.size > 10 * 1024 * 1024) {
        setError("File size exceeds 10MB limit.");
        return;
      }
      setImageFile(file);
      setImagePreview(URL.createObjectURL(file));
    }
  };

  const removeSelectedImage = () => {
    setImageFile(null);
    setImagePreview(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handleSend = async (textToSend) => {
    const text = textToSend || input;
    if (!text.trim() && !imageFile) return;

    setError("");
    if (!textToSend) setInput("");

    setLoading(true);

    try {
      // Case 1: Image Upload (Diagnostic Call)
      if (imageFile) {
        const userMsg = {
          role: "user",
          text: text || `Diagnose image (${imageAnimal})`,
          image: imagePreview,
        };
        setMessages((prev) => [...prev, userMsg]);

        const formData = new FormData();
        formData.append("file", imageFile);
        formData.append("animal_type", imageAnimal);
        formData.append("lang", language);
        if (activeSessionId) {
          formData.append("session_id", activeSessionId);
        }

        removeSelectedImage();

        const res = await api.post("/api/chat/image", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });

        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            text: res.data.response,
            imageUrl: res.data.image_url,
          },
        ]);

        if (res.data.session_id) {
          setActiveSessionId(res.data.session_id);
          fetchSessions();
        }
      } 
      // Case 2: Standard Text Chat Query
      else {
        const userMsg = { role: "user", text };
        setMessages((prev) => [...prev, userMsg]);

        const payload = {
          message: text,
          lang: language,
        };

        if (activeSessionId) {
          payload.session_id = activeSessionId;
        }

        const res = await api.post("/api/chat", payload);

        setMessages((prev) => [
          ...prev,
          { role: "assistant", text: res.data.response },
        ]);

        if (!activeSessionId && res.data.session_id) {
          setActiveSessionId(res.data.session_id);
        }
        
        // Refresh sessions sidebar list
        fetchSessions();
      }
    } catch (err) {
      console.error(err);
      setError(
        err.response?.data?.detail ||
          "Could not connect to the AI Assistant. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleSpeech = (text, index) => {
    if (!("speechSynthesis" in window)) {
      alert("Text-to-speech is not supported in this browser.");
      return;
    }

    if (speakingId === index) {
      window.speechSynthesis.cancel();
      setSpeakingId(null);
      return;
    }

    window.speechSynthesis.cancel();

    // Remove markdown formatting before speaking
    const cleanText = text.replace(/[*#_`~-]/g, "").trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);

    if (language === "hi") {
      utterance.lang = "hi-IN";
    } else if (language === "kn") {
      utterance.lang = "kn-IN";
    } else {
      utterance.lang = "en-IN";
    }

    utterance.onend = () => {
      setSpeakingId(null);
    };

    utterance.onerror = () => {
      setSpeakingId(null);
    };

    setSpeakingId(index);
    window.speechSynthesis.speak(utterance);
  };

  const formatText = (text) => {
    return text.split("\n").map((line, i) => {
      let content = line;
      const boldRegex = /\*\*(.*?)\*\*/g;
      const parts = [];
      let lastIdx = 0;
      let match;

      while ((match = boldRegex.exec(line)) !== null) {
        if (match.index > lastIdx) {
          parts.push(line.substring(lastIdx, match.index));
        }
        parts.push(
          <strong key={match.index} className="font-extrabold text-emerald-400">
            {match[1]}
          </strong>
        );
        lastIdx = boldRegex.lastIndex;
      }
      if (lastIdx < line.length) {
        parts.push(line.substring(lastIdx));
      }

      const finalLine = parts.length > 0 ? parts : content;

      if (line.startsWith("- ") || line.startsWith("* ")) {
        return (
          <li key={i} className="ml-4 list-disc text-slate-300 my-1">
            {parts.length > 0 ? parts : line.substring(2)}
          </li>
        );
      }
      return (
        <p key={i} className="my-1.5 leading-relaxed text-slate-200">
          {finalLine}
        </p>
      );
    });
  };

  const questionsList = quickQuestions[language] || quickQuestions["en"];

  return (
    <div className="bg-slate-950 text-white min-h-[calc(100vh-8rem)] py-6 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      {/* Background visual glows */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-emerald-500/5 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-teal-500/5 rounded-full blur-3xl pointer-events-none"></div>

      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-4 gap-6 relative z-10">
        
        {/* Mobile Sidebar Overlay */}
        <AnimatePresence>
          {mobileSidebarOpen && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 0.5 }}
              exit={{ opacity: 0 }}
              onClick={() => setMobileSidebarOpen(false)}
              className="fixed inset-0 bg-black z-40 lg:hidden"
            />
          )}
        </AnimatePresence>

        {/* Sidebar Panel (Sessions & Quick suggestions) */}
        <div className={`
          fixed inset-y-0 left-0 w-80 bg-slate-900 border-r border-slate-800 p-5 z-50 flex flex-col space-y-6 transform transition-transform duration-300 ease-in-out
          lg:relative lg:transform-none lg:inset-auto lg:w-auto lg:bg-transparent lg:border-none lg:p-0 lg:z-auto lg:flex
          ${mobileSidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"}
        `}>
          <div className="flex justify-between items-center lg:hidden">
            <span className="font-extrabold text-emerald-400 flex items-center gap-2 text-sm">
              <Bot className="w-5 h-5" /> PashuCare AI
            </span>
            <button 
              onClick={() => setMobileSidebarOpen(false)}
              className="p-1 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* New Chat Button */}
          <button
            onClick={startNewChat}
            className="w-full flex items-center justify-center gap-2 py-3 bg-linear-to-r from-emerald-500/10 to-teal-500/10 hover:from-emerald-500/20 hover:to-teal-500/20 border border-emerald-500/30 text-emerald-450 hover:text-white font-extrabold rounded-2xl transition-all shadow-lg hover:shadow-emerald-500/5 duration-350 cursor-pointer"
          >
            <Plus className="w-4 h-4" />
            <span>{localT.newChat}</span>
          </button>

          {/* Chat Sessions List */}
          <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-5 shadow-xl flex flex-col flex-1 min-h-[250px] max-h-[350px] lg:max-h-none overflow-hidden">
            <div className="flex items-center space-x-2 text-slate-400 font-bold border-b border-slate-800 pb-3 mb-3 text-xs uppercase tracking-wider">
              <MessageSquare className="w-4 h-4 text-emerald-450" />
              <span>{localT.history}</span>
            </div>
            
            <div className="flex-1 overflow-y-auto space-y-2 pr-1 custom-scrollbar">
              {sessions.length === 0 ? (
                <div className="text-center text-xs py-10 text-slate-500 font-medium">
                  {localT.noSessions}
                </div>
              ) : (
                sessions.map((s) => {
                  const isActive = activeSessionId === s.id;
                  return (
                    <div
                      key={s.id}
                      onClick={() => selectSession(s.id)}
                      className={`group relative flex items-center justify-between p-3 rounded-2xl border transition-all cursor-pointer ${
                        isActive
                          ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-400"
                          : "bg-slate-950/40 border-slate-850 text-slate-400 hover:bg-slate-800/40 hover:text-slate-200 hover:border-slate-750"
                      }`}
                    >
                      <div className="flex items-center space-x-2.5 overflow-hidden w-full pr-6">
                        <MessageSquare className={`w-3.5 h-3.5 shrink-0 ${isActive ? "text-emerald-400" : "text-slate-500"}`} />
                        <span className="text-xs font-semibold truncate block">
                          {s.title || "Untitled Chat"}
                        </span>
                      </div>
                      
                      <button
                        onClick={(e) => deleteSession(s.id, e)}
                        className="absolute right-2 opacity-0 group-hover:opacity-100 p-1.5 hover:bg-red-500/20 text-slate-500 hover:text-red-400 rounded-lg transition-all"
                        title="Delete Session"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  );
                })
              )}
            </div>
          </div>

          {/* Quick Suggestions Panel */}
          <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-5 shadow-xl flex flex-col space-y-4">
            <div className="flex items-center space-x-2 text-emerald-400 font-bold border-b border-slate-800 pb-3">
              <HelpCircle className="w-4 h-4" />
              <span className="text-xs uppercase tracking-wider">{localT.quickQuestions}</span>
            </div>
            <div className="flex flex-col space-y-2 max-h-[180px] overflow-y-auto pr-1">
              {questionsList.map((q, idx) => (
                <button
                  key={idx}
                  onClick={() => !loading && handleSend(q)}
                  disabled={loading}
                  className="text-left text-xs p-3 rounded-xl border border-slate-850 bg-slate-950 text-slate-400 hover:bg-slate-800 hover:text-white transition-all disabled:opacity-50 disabled:cursor-not-allowed hover:border-emerald-500/30"
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Main Chat Area */}
        <div className="lg:col-span-3 flex flex-col bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl h-[680px] overflow-hidden relative">
          
          {/* Chat Header */}
          <div className="bg-slate-850/80 backdrop-blur-md border-b border-slate-800 px-6 py-4 flex items-center justify-between">
            <div className="flex items-center space-x-3">
              {/* Mobile Menu Trigger */}
              <button 
                onClick={() => setMobileSidebarOpen(true)}
                className="lg:hidden p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition"
              >
                <Menu className="w-5 h-5" />
              </button>

              <div className="w-10 h-10 rounded-xl bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center text-slate-950 font-bold shadow-lg shadow-emerald-500/10">
                <Bot className="w-5 h-5 text-slate-950" />
              </div>
              <div>
                <h2 className="text-sm sm:text-base font-extrabold text-white flex items-center gap-1.5">
                  {localT.chat}
                  <span className="flex h-2 w-2 relative">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                  </span>
                </h2>
                <span className="text-[10px] text-slate-400 font-medium tracking-wide uppercase">Veterinary AI Assistant</span>
              </div>
            </div>

            {/* Language Switcher pills in Header */}
            <div className="flex items-center space-x-2">
              <div className="hidden sm:flex bg-slate-950/80 border border-slate-850 rounded-xl p-1 items-center space-x-1">
                <button
                  onClick={() => setLanguage("en")}
                  className={`px-2.5 py-1 text-[10px] font-extrabold rounded-lg transition-all ${
                    language === "en" ? "bg-emerald-500 text-slate-950 shadow-md" : "text-slate-400 hover:text-white"
                  }`}
                >
                  🇬🇧 EN
                </button>
                <button
                  onClick={() => setLanguage("hi")}
                  className={`px-2.5 py-1 text-[10px] font-extrabold rounded-lg transition-all ${
                    language === "hi" ? "bg-emerald-500 text-slate-950 shadow-md" : "text-slate-400 hover:text-white"
                  }`}
                >
                  🇮🇳 HI
                </button>
                <button
                  onClick={() => setLanguage("kn")}
                  className={`px-2.5 py-1 text-[10px] font-extrabold rounded-lg transition-all ${
                    language === "kn" ? "bg-emerald-500 text-slate-950 shadow-md" : "text-slate-400 hover:text-white"
                  }`}
                >
                  🇮🇳 KN
                </button>
              </div>
              
              {/* Mobile Language Toggle */}
              <div className="sm:hidden flex bg-slate-950 border border-slate-850 rounded-lg p-1.5 items-center">
                <select
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                  className="bg-transparent text-xs text-emerald-450 font-bold border-none focus:outline-none focus:ring-0"
                >
                  <option value="en" className="bg-slate-900 text-white">🇬🇧 EN</option>
                  <option value="hi" className="bg-slate-900 text-white">🇮🇳 हिन्दी</option>
                  <option value="kn" className="bg-slate-900 text-white">🇮🇳 ಕನ್ನಡ</option>
                </select>
              </div>
            </div>
          </div>

          {/* Chat Messages viewport */}
          <div className="flex-1 overflow-y-auto p-6 space-y-6 bg-[radial-gradient(circle_at_bottom_right,_var(--tw-gradient-stops))] from-emerald-950/5 via-slate-900 to-slate-900 custom-scrollbar">
            {error && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-2xl p-4 text-red-400 text-xs flex items-center space-x-2">
                <AlertCircle className="w-4 h-4 shrink-0" />
                <span>{error}</span>
              </div>
            )}

            <AnimatePresence initial={false}>
              {messages.map((msg, index) => {
                const isUser = msg.role === "user";
                return (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 15 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.25 }}
                    className={`flex items-start gap-3.5 ${
                      isUser ? "justify-end" : "justify-start"
                    }`}
                  >
                    {/* Assistant Avatar */}
                    {!isUser && (
                      <div className="w-8 h-8 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 mt-1 shadow-inner">
                        <Bot className="w-4.5 h-4.5" />
                      </div>
                    )}

                    <div className="group relative max-w-[80%] flex flex-col space-y-1">
                      {/* Message Bubble */}
                      <div
                        className={`px-4.5 py-3 rounded-2xl text-sm shadow-sm leading-relaxed ${
                          isUser
                            ? "bg-slate-800 text-slate-100 border border-slate-750 rounded-tr-sm"
                            : "bg-slate-950/90 text-slate-200 border border-slate-850 rounded-tl-sm"
                        }`}
                      >
                        {/* Render Local user uploaded Image */}
                        {isUser && msg.image && (
                          <div className="mb-2 max-w-sm rounded-xl overflow-hidden border border-slate-700 shadow-md">
                            <img
                              src={msg.image}
                              alt="Uploaded visual feed"
                              className="max-h-48 object-cover w-full"
                            />
                          </div>
                        )}

                        {/* Render Diagnosed Return Image from Backend */}
                        {!isUser && msg.imageUrl && (
                          <div className="mb-2 max-w-sm rounded-xl overflow-hidden border border-slate-850 shadow-md">
                            <img
                              src={`${API_BASE_URL}${msg.imageUrl}`}
                              alt="AI diagnosed visual feed"
                              className="max-h-48 object-cover w-full"
                            />
                          </div>
                        )}

                        {isUser ? msg.text : formatText(msg.text)}
                        
                        {/* Show Nearby Vets Button if this is a diagnosis (has image) */}
                        {!isUser && msg.imageUrl && (
                          <div className="mt-4 border-t border-slate-700/50 pt-3">
                            <Link
                              to="/vets"
                              className="inline-flex items-center space-x-2 px-3 py-1.5 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 text-xs font-bold rounded-lg border border-emerald-500/30 transition-colors"
                            >
                              <MapPin className="w-3.5 h-3.5" />
                              <span>{localT.nearbyVetsBtn}</span>
                            </Link>
                          </div>
                        )}
                      </div>

                      {/* Controls (Speak button for Assistant) */}
                      {!isUser && (
                        <div className="flex items-center space-x-2 pl-1 opacity-0 group-hover:opacity-100 transition-opacity">
                          <button
                            onClick={() => handleSpeech(msg.text, index)}
                            className={`flex items-center space-x-1 text-[10px] font-bold p-1 rounded-lg hover:bg-slate-800 transition-colors cursor-pointer ${
                              speakingId === index
                                ? "text-emerald-400 bg-emerald-500/10 px-2 py-0.5 border border-emerald-500/20"
                                : "text-slate-500 hover:text-slate-200"
                            }`}
                          >
                            {speakingId === index ? (
                              <>
                                <VolumeX className="w-3 h-3 animate-pulse" />
                                <span>{localT.stop}</span>
                              </>
                            ) : (
                              <>
                                <Volume2 className="w-3 h-3" />
                                <span>{localT.listen}</span>
                              </>
                            )}
                          </button>
                        </div>
                      )}
                    </div>

                    {/* User Avatar */}
                    {isUser && (
                      <div className="w-8 h-8 rounded-xl bg-slate-800 border border-slate-750 flex items-center justify-center text-slate-350 shrink-0 mt-1 shadow-inner">
                        <User className="w-4.5 h-4.5" />
                      </div>
                    )}
                  </motion.div>
                );
              })}

              {/* Typing/Loading Indicator */}
              {loading && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="flex items-start gap-3.5 justify-start"
                >
                  <div className="w-8 h-8 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 mt-1 shadow-inner">
                    <Bot className="w-4.5 h-4.5" />
                  </div>
                  <div className="px-4 py-3 rounded-2xl bg-slate-950 border border-slate-850 text-slate-100 rounded-tl-sm flex items-center space-x-1.5 shadow-sm">
                    <span className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce [animation-delay:-0.3s]"></span>
                    <span className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce [animation-delay:-0.15s]"></span>
                    <span className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce"></span>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            <div ref={messagesEndRef} />
          </div>

          {/* Image Selected Preview Panel */}
          {imagePreview && (
            <div className="bg-slate-900 border-t border-slate-850 px-6 py-3 flex items-center justify-between gap-4">
              <div className="flex items-center space-x-3">
                <div className="relative w-12 h-12 rounded-lg overflow-hidden border border-emerald-500/30">
                  <img src={imagePreview} alt="attachment preview" className="w-full h-full object-cover" />
                  <button
                    onClick={removeSelectedImage}
                    className="absolute -top-1 -right-1 bg-red-500 text-slate-50 rounded-full p-0.5 hover:bg-red-600 transition shadow"
                  >
                    <X className="w-3 h-3" />
                  </button>
                </div>
                <div>
                  <span className="text-xs font-semibold block text-slate-200">{localT.imageAttached}</span>
                  <span className="text-[10px] text-slate-500">{localT.readyDiagnosis}</span>
                </div>
              </div>

              {/* Animal Type Select Selector */}
              <div className="flex items-center space-x-2">
                <label className="text-xs text-slate-400 font-semibold">{localT.animalType}</label>
                <select
                  value={imageAnimal}
                  onChange={(e) => setImageAnimal(e.target.value)}
                  className="bg-slate-950 border border-slate-800 text-xs font-bold text-emerald-400 rounded-lg px-2 py-1.5 focus:outline-none focus:border-emerald-500 cursor-pointer"
                >
                  <option value="Cow">🐄 Cow</option>
                  <option value="Goat">🐐 Goat</option>
                  <option value="Sheep">🐏 Sheep</option>
                </select>
              </div>
            </div>
          )}

          {/* Chat Input Form */}
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSend();
            }}
            className="bg-slate-900 border-t border-slate-800 p-4 flex gap-3 items-center"
          >
            {/* Attachment Button */}
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              disabled={loading}
              className="p-3 text-slate-450 hover:text-emerald-400 hover:bg-slate-800 rounded-xl transition-colors border border-slate-800 bg-slate-950 cursor-pointer shrink-0 disabled:opacity-50 disabled:cursor-not-allowed"
              title="Attach photo for diagnostics"
            >
              <Paperclip className="w-4.5 h-4.5" />
            </button>
            <input
              type="file"
              ref={fileInputRef}
              accept="image/*,.heic,.heif,.webp,.bmp"
              onChange={handleImageChange}
              className="hidden"
            />

            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={imagePreview ? "Type details (optional) and send..." : localT.chatPlaceholder}
              disabled={loading}
              className="grow px-4 py-3 text-sm bg-slate-950 border border-slate-800 text-white rounded-xl focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 focus:outline-none transition-all placeholder-slate-500 disabled:opacity-60"
            />
            <button
              type="submit"
              disabled={loading || (!input.trim() && !imageFile)}
              className="px-4.5 py-3 bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-extrabold rounded-xl transition-all shadow-md shadow-emerald-500/10 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center cursor-pointer shrink-0"
            >
              <Send className="w-4 h-4 text-slate-950" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;

