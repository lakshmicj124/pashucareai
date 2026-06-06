import { useState, useEffect, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Activity, AlertTriangle, Bell, ChevronDown, ChevronRight, Globe,
  Heart, Home, LogOut, Menu, Mic, MicOff, Moon, Sun, Upload,
  User, Users, X, Check, Stethoscope, Shield, Zap, TrendingUp,
  Camera, FileText, Settings, PlusCircle, Search, RefreshCw,
  BarChart2, Eye, Clock, Phone, Star, Leaf, Droplets, Thermometer,
  CheckCircle, XCircle, Info, ChevronLeft, Wind
} from "lucide-react";
import {
  LineChart, Line, AreaChart, Area, BarChart, Bar, PieChart, Pie, Cell,
  RadialBarChart, RadialBar, XAxis, YAxis, CartesianGrid, Tooltip,
  Legend, ResponsiveContainer
} from "recharts";

// ─── TRANSLATIONS ─────────────────────────────────────────────────────────────
const T = {
  en: {
    appName: "PashuCare AI", tagline: "AI-Powered Livestock Health Assistant",
    login: "Login", register: "Register", farmer: "Farmer", vet: "Veterinarian",
    admin: "Admin", email: "Email", password: "Password", name: "Full Name",
    dashboard: "Dashboard", animals: "My Animals", diagnosis: "AI Diagnosis",
    notifications: "Notifications", reports: "Reports", settings: "Settings",
    logout: "Logout", uploadImage: "Upload Image", analyzeDisease: "Analyze Disease",
    confidence: "Confidence", severity: "Severity", symptoms: "Symptoms",
    causes: "Causes", prevention: "Prevention", firstAid: "First Aid",
    addAnimal: "Add Animal", animalId: "Animal ID", breed: "Breed",
    age: "Age", weight: "Weight (kg)", emergency: "EMERGENCY ALERT",
    callVet: "Call Vet Now", dismiss: "Dismiss", darkMode: "Dark Mode",
    language: "Language", healthy: "Healthy", sick: "Sick", critical: "Critical",
    totalAnimals: "Total Animals", healthAlerts: "Health Alerts",
    recentDiagnoses: "Recent Diagnoses", activeVets: "Active Vets",
    voiceAssistant: "Voice Assistant", speaking: "Listening...",
    diseaseDetected: "Disease Detected", noDisease: "No Disease Found",
    cow: "Cow", goat: "Goat", sheep: "Sheep",
    heroTitle: "Smart Health for Your Livestock", heroSubtitle: "AI-powered disease detection, real-time monitoring, and instant vet consultation for your farm animals.",
    getStarted: "Get Started Free", learnMore: "Learn More",
    feature1: "AI Disease Detection", feature1Desc: "Upload a photo for instant diagnosis",
    feature2: "24/7 Monitoring", feature2Desc: "Real-time health tracking alerts",
    feature3: "Vet Network", feature3Desc: "Connect with certified vets instantly",
    signInContinue: "Sign in to continue", createAccount: "Create your account",
    alreadyAccount: "Already have an account?", noAccount: "Don't have an account?",
    role: "I am a", welcomeBack: "Welcome back",
    profilePic: "Profile Photo", lastCheckup: "Last Checkup",
    healthScore: "Health Score", vaccineStatus: "Vaccine Status", due: "Due",
    upToDate: "Up to date", overdue: "Overdue"
  },
  kn: {
    appName: "ಪಶುಕೇರ್ AI", tagline: "AI ಆಧಾರಿತ ಜಾನುವಾರು ಆರೋಗ್ಯ ಸಹಾಯಕ",
    login: "ಲಾಗಿನ್", register: "ನೋಂದಾಯಿಸಿ", farmer: "ರೈತ", vet: "ಪಶುವೈದ್ಯ",
    admin: "ನಿರ್ವಾಹಕ", email: "ಇಮೇಲ್", password: "ಗುಪ್ತಪದ", name: "ಪೂರ್ಣ ಹೆಸರು",
    dashboard: "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", animals: "ನನ್ನ ಪ್ರಾಣಿಗಳು", diagnosis: "AI ರೋಗನಿರ್ಣಯ",
    notifications: "ಅಧಿಸೂಚನೆಗಳು", reports: "ವರದಿಗಳು", settings: "ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
    logout: "ಲಾಗ್ ಔಟ್", uploadImage: "ಚಿತ್ರ ಅಪ್‌ಲೋಡ್", analyzeDisease: "ರೋಗ ವಿಶ್ಲೇಷಿಸಿ",
    confidence: "ವಿಶ್ವಾಸ", severity: "ತೀವ್ರತೆ", symptoms: "ಲಕ್ಷಣಗಳು",
    causes: "ಕಾರಣಗಳು", prevention: "ತಡೆಗಟ್ಟುವಿಕೆ", firstAid: "ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ",
    addAnimal: "ಪ್ರಾಣಿ ಸೇರಿಸಿ", animalId: "ಪ್ರಾಣಿ ID", breed: "ತಳಿ",
    age: "ವಯಸ್ಸು", weight: "ತೂಕ (kg)", emergency: "ತುರ್ತು ಎಚ್ಚರಿಕೆ",
    callVet: "ಈಗ ಪಶುವೈದ್ಯರನ್ನು ಕರೆಯಿರಿ", dismiss: "ತಳ್ಳಿಹಾಕಿ", darkMode: "ಡಾರ್ಕ್ ಮೋಡ್",
    language: "ಭಾಷೆ", healthy: "ಆರೋಗ್ಯಕರ", sick: "ಅನಾರೋಗ್ಯ", critical: "ನಿರ್ಣಾಯಕ",
    totalAnimals: "ಒಟ್ಟು ಪ್ರಾಣಿಗಳು", healthAlerts: "ಆರೋಗ್ಯ ಎಚ್ಚರಿಕೆಗಳು",
    recentDiagnoses: "ಇತ್ತೀಚಿನ ರೋಗನಿರ್ಣಯ", activeVets: "ಸಕ್ರಿಯ ಪಶುವೈದ್ಯರು",
    voiceAssistant: "ಧ್ವನಿ ಸಹಾಯಕ", speaking: "ಆಲಿಸುತ್ತಿದ್ದೇನೆ...",
    diseaseDetected: "ರೋಗ ಪತ್ತೆಯಾಗಿದೆ", noDisease: "ರೋಗ ಕಂಡುಬಂದಿಲ್ಲ",
    cow: "ಹಸು", goat: "ಆಡು", sheep: "ಕುರಿ",
    heroTitle: "ನಿಮ್ಮ ಜಾನುವಾರುಗಳಿಗೆ ಸ್ಮಾರ್ಟ್ ಆರೋಗ್ಯ", heroSubtitle: "AI ಆಧಾರಿತ ರೋಗ ಪತ್ತೆ, ನೈಜ-ಸಮಯ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ತ್ವರಿತ ಪಶುವೈದ್ಯ ಸಲಹೆ.",
    getStarted: "ಉಚಿತವಾಗಿ ಪ್ರಾರಂಭಿಸಿ", learnMore: "ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ",
    feature1: "AI ರೋಗ ಪತ್ತೆ", feature1Desc: "ತ್ವರಿತ ರೋಗನಿರ್ಣಯಕ್ಕಾಗಿ ಫೋಟೋ ಅಪ್‌ಲೋಡ್",
    feature2: "24/7 ಮೇಲ್ವಿಚಾರಣೆ", feature2Desc: "ನೈಜ-ಸಮಯ ಆರೋಗ್ಯ ಟ್ರ್ಯಾಕಿಂಗ್",
    feature3: "ಪಶುವೈದ್ಯ ನೆಟ್‌ವರ್ಕ್", feature3Desc: "ಪ್ರಮಾಣೀಕೃತ ಪಶುವೈದ್ಯರೊಂದಿಗೆ ಸಂಪರ್ಕ",
    signInContinue: "ಮುಂದುವರಿಯಲು ಸೈನ್ ಇನ್ ಮಾಡಿ", createAccount: "ನಿಮ್ಮ ಖಾತೆ ರಚಿಸಿ",
    alreadyAccount: "ಈಗಾಗಲೇ ಖಾತೆ ಇದೆಯೇ?", noAccount: "ಖಾತೆ ಇಲ್ಲವೇ?",
    role: "ನಾನು", welcomeBack: "ಮತ್ತೆ ಸ್ವಾಗತ",
    profilePic: "ಪ್ರೊಫೈಲ್ ಫೋಟೋ", lastCheckup: "ಕೊನೆಯ ತಪಾಸಣೆ",
    healthScore: "ಆರೋಗ್ಯ ಸ್ಕೋರ್", vaccineStatus: "ಲಸಿಕೆ ಸ್ಥಿತಿ",
    due: "ಬಾಕಿ ಇದೆ", upToDate: "ನವೀಕೃತ", overdue: "ಅವಧಿ ಮೀರಿದೆ"
  },
  hi: {
    appName: "पशुकेयर AI", tagline: "AI-संचालित पशुधन स्वास्थ्य सहायक",
    login: "लॉग इन", register: "रजिस्टर", farmer: "किसान", vet: "पशुचिकित्सक",
    admin: "व्यवस्थापक", email: "ईमेल", password: "पासवर्ड", name: "पूरा नाम",
    dashboard: "डैशबोर्ड", animals: "मेरे पशु", diagnosis: "AI निदान",
    notifications: "सूचनाएं", reports: "रिपोर्ट", settings: "सेटिंग्स",
    logout: "लॉग आउट", uploadImage: "छवि अपलोड करें", analyzeDisease: "रोग विश्लेषण",
    confidence: "विश्वास", severity: "गंभीरता", symptoms: "लक्षण",
    causes: "कारण", prevention: "रोकथाम", firstAid: "प्राथमिक उपचार",
    addAnimal: "पशु जोड़ें", animalId: "पशु ID", breed: "नस्ल",
    age: "उम्र", weight: "वजन (kg)", emergency: "आपातकालीन चेतावनी",
    callVet: "अभी पशुचिकित्सक को बुलाएं", dismiss: "खारिज करें", darkMode: "डार्क मोड",
    language: "भाषा", healthy: "स्वस्थ", sick: "बीमार", critical: "गंभीर",
    totalAnimals: "कुल पशु", healthAlerts: "स्वास्थ्य चेतावनियां",
    recentDiagnoses: "हालिया निदान", activeVets: "सक्रिय पशुचिकित्सक",
    voiceAssistant: "वॉइस असिस्टेंट", speaking: "सुन रहा हूं...",
    diseaseDetected: "रोग पता चला", noDisease: "कोई रोग नहीं मिला",
    cow: "गाय", goat: "बकरी", sheep: "भेड़",
    heroTitle: "अपने पशुओं के लिए स्मार्ट स्वास्थ्य", heroSubtitle: "AI-संचालित रोग पहचान, रियल-टाइम निगरानी और तुरंत पशुचिकित्सक परामर्श।",
    getStarted: "मुफ्त शुरू करें", learnMore: "और जानें",
    feature1: "AI रोग पहचान", feature1Desc: "तुरंत निदान के लिए फोटो अपलोड करें",
    feature2: "24/7 निगरानी", feature2Desc: "रियल-टाइम स्वास्थ्य ट्रैकिंग अलर्ट",
    feature3: "पशुचिकित्सक नेटवर्क", feature3Desc: "प्रमाणित पशुचिकित्सकों से जुड़ें",
    signInContinue: "जारी रखने के लिए साइन इन करें", createAccount: "अपना खाता बनाएं",
    alreadyAccount: "पहले से खाता है?", noAccount: "खाता नहीं है?",
    role: "मैं हूं", welcomeBack: "वापस स्वागत है",
    profilePic: "प्रोफाइल फोटो", lastCheckup: "अंतिम जांच",
    healthScore: "स्वास्थ्य स्कोर", vaccineStatus: "टीका स्थिति",
    due: "बकाया", upToDate: "अद्यतन", overdue: "समय सीमा पार"
  }
};

// ─── MOCK DATA ─────────────────────────────────────────────────────────────────
const DISEASES = [
  {
    id: 1, name: "Foot and Mouth Disease", animal: "Cow", confidence: 94, severity: "Critical",
    severityColor: "red",
    symptoms: ["Fever above 40°C", "Blisters on mouth and hooves", "Excessive salivation", "Lameness", "Loss of appetite"],
    causes: ["Picornavirus (FMDV)", "Direct contact with infected animals", "Contaminated feed or water", "Airborne transmission"],
    prevention: ["Regular vaccination every 6 months", "Quarantine new animals for 14 days", "Disinfect farm equipment", "Restrict visitor access"],
    firstAid: ["Isolate the animal immediately", "Clean lesions with antiseptic", "Provide soft feed and clean water", "Call veterinarian urgently", "Do not move animals off-farm"]
  },
  {
    id: 2, name: "Mastitis", animal: "Cow", confidence: 87, severity: "Moderate",
    severityColor: "amber",
    symptoms: ["Swollen udder", "Hot and painful teats", "Abnormal milk (clots/blood)", "Reduced milk production", "Mild fever"],
    causes: ["Bacterial infection (Staph, Strep)", "Poor milking hygiene", "Teat injuries", "Environmental contamination"],
    prevention: ["Pre and post-dip teats after milking", "Maintain clean bedding", "Regular udder health checks", "Dry cow therapy"],
    firstAid: ["Strip affected quarters", "Apply cold compress to reduce swelling", "Ensure clean environment", "Consult vet for antibiotics"]
  },
  {
    id: 3, name: "Goat Pox", animal: "Goat", confidence: 91, severity: "High",
    severityColor: "orange",
    symptoms: ["Skin lesions and pox scabs", "High fever (41-42°C)", "Nasal discharge", "Swollen lymph nodes", "Difficulty breathing"],
    causes: ["Capripoxvirus", "Direct contact with infected goats", "Insects as mechanical vectors", "Contaminated environment"],
    prevention: ["Annual vaccination", "Quarantine infected animals", "Vector control (flies, mosquitoes)", "Disinfect housing regularly"],
    firstAid: ["Isolate affected animals", "Treat secondary infections with antibiotics", "Apply antiseptic to lesions", "Supportive care — fluids and nutrition"]
  },
  {
    id: 4, name: "Sheep Scab", animal: "Sheep", confidence: 78, severity: "Moderate",
    severityColor: "amber",
    symptoms: ["Intense itching and rubbing", "Wool loss", "Yellow/crusty scabs on skin", "Restlessness", "Weight loss"],
    causes: ["Psoroptes ovis mite infestation", "Direct contact between sheep", "Shared equipment or housing"],
    prevention: ["Regular dipping or pour-on treatments", "Quarantine new stock for 4 weeks", "Regular flock inspection", "Treat all animals simultaneously"],
    firstAid: ["Separate affected sheep", "Apply approved acaricide treatment", "Treat entire flock within 14 days", "Notify authorities (notifiable in some regions)"]
  },
  {
    id: 5, name: "Bloat", animal: "Cow", confidence: 82, severity: "High",
    severityColor: "orange",
    symptoms: ["Distended left flank", "Labored breathing", "Kicking at belly", "Excessive drooling", "Sudden death if untreated"],
    causes: ["Legume-rich pasture (clover/alfalfa)", "Grain overload", "Esophageal obstruction", "Change in diet too quickly"],
    prevention: ["Gradual diet transitions", "Limit legume pasture access", "Provide roughage before grazing", "Anti-bloat blocks or oils"],
    firstAid: ["Walk the animal slowly", "Pass stomach tube to release gas", "Anti-foaming agents (poloxalene)", "Position head uphill if lying down", "Call vet immediately for severe cases"]
  }
];

const MOCK_ANIMALS = [
  { id: "C001", name: "Lakshmi", type: "Cow", breed: "Holstein Friesian", age: 4, weight: 520, status: "Healthy", healthScore: 92, lastCheckup: "2025-05-15", vaccineStatus: "upToDate", image: "🐄" },
  { id: "C002", name: "Nandini", type: "Cow", breed: "Gir", age: 6, weight: 480, status: "Sick", healthScore: 64, lastCheckup: "2025-05-20", vaccineStatus: "due", image: "🐄" },
  { id: "G001", name: "Kali", type: "Goat", breed: "Beetal", age: 2, weight: 38, status: "Healthy", healthScore: 88, lastCheckup: "2025-04-30", vaccineStatus: "upToDate", image: "🐐" },
  { id: "G002", name: "Meena", type: "Goat", breed: "Boer", age: 3, weight: 45, status: "Critical", healthScore: 41, lastCheckup: "2025-05-22", vaccineStatus: "overdue", image: "🐐" },
  { id: "S001", name: "Bholi", type: "Sheep", breed: "Merino", age: 2, weight: 62, status: "Healthy", healthScore: 95, lastCheckup: "2025-05-10", vaccineStatus: "upToDate", image: "🐑" },
  { id: "S002", name: "Rupa", type: "Sheep", breed: "Deccani", age: 5, weight: 55, status: "Sick", healthScore: 71, lastCheckup: "2025-05-18", vaccineStatus: "due", image: "🐑" },
];

const HEALTH_TREND = [
  { month: "Jan", healthy: 18, sick: 3, critical: 1 },
  { month: "Feb", healthy: 20, sick: 2, critical: 0 },
  { month: "Mar", healthy: 17, sick: 4, critical: 2 },
  { month: "Apr", healthy: 22, sick: 1, critical: 0 },
  { month: "May", healthy: 19, sick: 3, critical: 1 },
  { month: "Jun", healthy: 21, sick: 2, critical: 1 },
];

const DISEASE_DISTRIBUTION = [
  { name: "Mastitis", value: 32, color: "#10b981" },
  { name: "FMD", value: 24, color: "#ef4444" },
  { name: "Bloat", value: 18, color: "#f59e0b" },
  { name: "Goat Pox", value: 15, color: "#3b82f6" },
  { name: "Others", value: 11, color: "#8b5cf6" },
];

const NOTIFICATIONS = [
  { id: 1, type: "critical", title: "Critical: Goat G002 Needs Immediate Attention", body: "Meena shows signs of Goat Pox — severity critical. Vet Dr. Priya notified.", time: "2 min ago", read: false },
  { id: 2, type: "warning", title: "Vaccine Due: Cow C002", body: "Nandini's FMD vaccine is overdue by 3 days. Schedule immediately.", time: "1 hr ago", read: false },
  { id: 3, type: "info", title: "AI Diagnosis Complete", body: "Sheep S002 (Rupa) analyzed — Sheep Scab detected with 78% confidence.", time: "3 hrs ago", read: true },
  { id: 4, type: "success", title: "Vet Visit Confirmed", body: "Dr. Ravi Kumar will visit your farm on May 25, 2025 at 10 AM.", time: "Yesterday", read: true },
  { id: 5, type: "info", title: "Monthly Health Report Ready", body: "Your farm's May 2025 health report is available for download.", time: "2 days ago", read: true },
];

const WEIGHT_TREND = [
  { week: "W1", cow: 510, goat: 36, sheep: 60 },
  { week: "W2", cow: 515, goat: 37, sheep: 61 },
  { week: "W3", cow: 512, goat: 38, sheep: 62 },
  { week: "W4", cow: 520, goat: 38, sheep: 62 },
  { week: "W5", cow: 518, goat: 39, sheep: 63 },
];

// ─── HELPER COMPONENTS ─────────────────────────────────────────────────────────

const Toast = ({ toasts, removeToast }) => (
  <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
    <AnimatePresence>
      {toasts.map(t => (
        <motion.div key={t.id} initial={{ opacity: 0, x: 80 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 80 }}
          className={`flex items-center gap-3 px-4 py-3 rounded-xl shadow-2xl text-white text-sm font-medium max-w-xs
            ${t.type === "success" ? "bg-emerald-600" : t.type === "error" ? "bg-red-600" : t.type === "warning" ? "bg-amber-500" : "bg-blue-600"}`}>
          {t.type === "success" ? <CheckCircle size={16} /> : t.type === "error" ? <XCircle size={16} /> : <Info size={16} />}
          <span>{t.message}</span>
          <button onClick={() => removeToast(t.id)} className="ml-auto opacity-70 hover:opacity-100"><X size={14} /></button>
        </motion.div>
      ))}
    </AnimatePresence>
  </div>
);

const GlassCard = ({ children, className = "", dark }) => (
  <div className={`rounded-2xl border backdrop-blur-sm
    ${dark ? "bg-gray-800/60 border-gray-700/50 shadow-lg shadow-black/20" : "bg-white/80 border-white/60 shadow-lg shadow-emerald-100/50"}
    ${className}`}>
    {children}
  </div>
);

const GradientBtn = ({ onClick, children, variant = "primary", className = "", disabled }) => {
  const variants = {
    primary: "bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-white shadow-lg shadow-emerald-500/30",
    danger: "bg-linear-to-r from-red-500 to-rose-600 hover:from-red-600 hover:to-rose-700 text-white shadow-lg shadow-red-500/30",
    outline: "border-2 border-emerald-500 text-emerald-600 hover:bg-emerald-50",
    secondary: "bg-linear-to-r from-blue-500 to-indigo-500 hover:from-blue-600 hover:to-indigo-600 text-white shadow-lg shadow-blue-500/30"
  };
  return (
    <motion.button whileHover={{ scale: disabled ? 1 : 1.02 }} whileTap={{ scale: disabled ? 1 : 0.97 }}
      onClick={onClick} disabled={disabled}
      className={`px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-200 ${variants[variant]} ${className} ${disabled ? "opacity-50 cursor-not-allowed" : "cursor-pointer"}`}>
      {children}
    </motion.button>
  );
};

const SeverityBadge = ({ level }) => {
  const map = { Critical: "bg-red-100 text-red-700 border-red-200", High: "bg-orange-100 text-orange-700 border-orange-200", Moderate: "bg-amber-100 text-amber-700 border-amber-200", Low: "bg-green-100 text-green-700 border-green-200" };
  return <span className={`px-3 py-1 rounded-full text-xs font-bold border ${map[level] || map.Low}`}>{level}</span>;
};

const StatusDot = ({ status, dark }) => {
  const map = { Healthy: "bg-emerald-400", Sick: "bg-amber-400", Critical: "bg-red-500" };
  return <span className={`inline-block w-2.5 h-2.5 rounded-full ${map[status] || "bg-gray-400"} ${status === "Critical" ? "animate-pulse" : ""}`} />;
};

const LoadingSpinner = ({ dark }) => (
  <div className="flex items-center justify-center p-8">
    <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
      className="w-10 h-10 rounded-full border-4 border-emerald-200 border-t-emerald-600" />
  </div>
);

// ─── LANDING PAGE ──────────────────────────────────────────────────────────────
const LandingPage = ({ onEnter, lang, dark }) => {
  const t = T[lang];
  return (
    <div className={`min-h-screen ${dark ? "bg-gray-950" : "bg-linear-to-br from-emerald-50 via-teal-50 to-cyan-50"} overflow-hidden`}>
      {/* Nav */}
      <nav className={`fixed top-0 w-full z-40 px-6 py-4 flex items-center justify-between backdrop-blur-md border-b ${dark ? "bg-gray-900/80 border-gray-800" : "bg-white/70 border-white/50"}`}>
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center shadow-lg shadow-emerald-500/30">
            <Leaf size={18} className="text-white" />
          </div>
          <span className={`font-bold text-lg ${dark ? "text-white" : "text-gray-900"}`}>{t.appName}</span>
        </div>
        <div className="flex items-center gap-3">
          <GradientBtn variant="outline" onClick={() => onEnter("login")} className="hidden sm:flex">{t.login}</GradientBtn>
          <GradientBtn onClick={() => onEnter("register")}>{t.register}</GradientBtn>
        </div>
      </nav>

      {/* Hero */}
      <section className="pt-28 pb-20 px-6 max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <motion.div initial={{ opacity: 0, y: 40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }}>
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-emerald-100 text-emerald-700 text-sm font-semibold mb-6 border border-emerald-200">
              <Zap size={14} /> AI-Powered • Real-time • Multilingual
            </div>
            <h1 className={`text-4xl md:text-5xl font-extrabold leading-tight mb-6 ${dark ? "text-white" : "text-gray-900"}`}>
              {t.heroTitle.split(" ").map((w, i) => (
                <span key={i} className={i >= 3 ? "text-transparent bg-clip-text bg-linear-to-r from-emerald-500 to-teal-500" : ""}>{w} </span>
              ))}
            </h1>
            <p className={`text-lg mb-8 leading-relaxed ${dark ? "text-gray-300" : "text-gray-600"}`}>{t.heroSubtitle}</p>
            <div className="flex flex-wrap gap-4">
              <GradientBtn onClick={() => onEnter("register")} className="text-base px-8 py-3">{t.getStarted}</GradientBtn>
              <GradientBtn variant="outline" onClick={() => onEnter("login")} className="text-base px-8 py-3">{t.learnMore}</GradientBtn>
            </div>
            <div className="mt-8 flex gap-6">
              {[["10K+", "Farmers"], ["50K+", "Animals Monitored"], ["98%", "Accuracy"]].map(([n, l]) => (
                <div key={l}>
                  <div className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{n}</div>
                  <div className="text-sm text-gray-500">{l}</div>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div initial={{ opacity: 0, x: 40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.8, delay: 0.2 }} className="relative">
            <div className={`rounded-3xl p-6 ${dark ? "bg-gray-800/80 border border-gray-700" : "bg-white/90 border border-emerald-100"} shadow-2xl shadow-emerald-200/40`}>
              <div className="flex items-center gap-3 mb-5">
                <div className="w-10 h-10 rounded-xl bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center">
                  <Activity size={20} className="text-white" />
                </div>
                <div>
                  <div className={`font-bold ${dark ? "text-white" : "text-gray-900"}`}>AI Diagnosis Result</div>
                  <div className="text-xs text-gray-500">Analyzed 2 seconds ago</div>
                </div>
                <span className="ml-auto px-3 py-1 rounded-full bg-red-100 text-red-600 text-xs font-bold">Critical</span>
              </div>
              <div className={`text-xl font-bold mb-1 ${dark ? "text-white" : "text-gray-900"}`}>Foot and Mouth Disease</div>
              <div className="flex items-center gap-2 mb-4">
                <div className="flex-1 h-3 rounded-full bg-gray-100 overflow-hidden">
                  <motion.div initial={{ width: 0 }} animate={{ width: "94%" }} transition={{ delay: 0.5, duration: 1 }}
                    className="h-full rounded-full bg-linear-to-r from-emerald-400 to-emerald-600" />
                </div>
                <span className="text-sm font-bold text-emerald-600">94%</span>
              </div>
              <div className="grid grid-cols-2 gap-3 text-sm">
                {["Fever 40°C+", "Mouth Blisters", "Lameness", "Loss of Appetite"].map(s => (
                  <div key={s} className="flex items-center gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                    <span className={dark ? "text-gray-300" : "text-gray-600"}>{s}</span>
                  </div>
                ))}
              </div>
              <div className="mt-4 p-3 rounded-xl bg-red-50 border border-red-100 flex items-start gap-2">
                <AlertTriangle size={16} className="text-red-500 mt-0.5 shrink-0" />
                <span className="text-xs text-red-600 font-medium">Immediate veterinary attention required. Isolate animal now.</span>
              </div>
            </div>
            {/* Floating badges */}
            <motion.div animate={{ y: [0, -8, 0] }} transition={{ repeat: Infinity, duration: 3 }}
              className="absolute -top-4 -right-4 bg-emerald-500 text-white px-3 py-2 rounded-xl text-xs font-bold shadow-lg shadow-emerald-500/40">
              🐄 Cow Analyzed
            </motion.div>
            <motion.div animate={{ y: [0, 8, 0] }} transition={{ repeat: Infinity, duration: 3.5 }}
              className="absolute -bottom-4 -left-4 bg-blue-500 text-white px-3 py-2 rounded-xl text-xs font-bold shadow-lg shadow-blue-500/40">
              📊 94% Confidence
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 px-6 max-w-6xl mx-auto">
        <motion.div initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}
          className="text-center mb-12">
          <h2 className={`text-3xl font-extrabold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Everything Your Farm Needs</h2>
          <p className={`text-lg ${dark ? "text-gray-400" : "text-gray-500"}`}>Comprehensive health management for Cows, Goats & Sheep</p>
        </motion.div>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { icon: Camera, title: t.feature1, desc: t.feature1Desc, color: "from-emerald-500 to-teal-500", bg: "bg-emerald-50" },
            { icon: Activity, title: t.feature2, desc: t.feature2Desc, color: "from-blue-500 to-indigo-500", bg: "bg-blue-50" },
            { icon: Stethoscope, title: t.feature3, desc: t.feature3Desc, color: "from-violet-500 to-purple-500", bg: "bg-violet-50" },
          ].map((f, i) => (
            <motion.div key={i} initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: i * 0.15 }}
              whileHover={{ y: -4, boxShadow: "0 20px 40px rgba(0,0,0,0.1)" }}
              className={`p-6 rounded-2xl border ${dark ? "bg-gray-800 border-gray-700" : "bg-white border-gray-100"} cursor-default`}>
              <div className={`w-12 h-12 rounded-xl bg-linear-to-br ${f.color} flex items-center justify-center mb-4 shadow-lg`}>
                <f.icon size={24} className="text-white" />
              </div>
              <h3 className={`text-lg font-bold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{f.title}</h3>
              <p className={`text-sm ${dark ? "text-gray-400" : "text-gray-500"}`}>{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Animal Types */}
      <section className="py-16 px-6 max-w-6xl mx-auto">
        <div className="grid grid-cols-3 gap-6">
          {[
            { emoji: "🐄", name: "Cow", count: "28 diseases", color: "emerald" },
            { emoji: "🐐", name: "Goat", count: "21 diseases", color: "teal" },
            { emoji: "🐑", name: "Sheep", count: "19 diseases", color: "cyan" }
          ].map((a, i) => (
            <motion.div key={i} whileHover={{ scale: 1.05 }} onClick={() => onEnter("register")}
              className={`p-6 rounded-2xl text-center cursor-pointer border ${dark ? "bg-gray-800 border-gray-700 hover:border-emerald-500" : "bg-white border-gray-100 hover:border-emerald-300"} transition-all shadow-lg`}>
              <div className="text-5xl mb-3">{a.emoji}</div>
              <div className={`font-bold text-lg ${dark ? "text-white" : "text-gray-900"}`}>{a.name}</div>
              <div className="text-sm text-emerald-600 font-medium">{a.count}</div>
            </motion.div>
          ))}
        </div>
      </section>
    </div>
  );
};

// ─── AUTH PAGE ─────────────────────────────────────────────────────────────────
const AuthPage = ({ mode, onAuth, onToggle, lang, dark }) => {
  const t = T[lang];
  const [role, setRole] = useState("farmer");
  const [form, setForm] = useState({ email: "", password: "", name: "" });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    await new Promise(r => setTimeout(r, 1200));
    setLoading(false);
    onAuth({ email: form.email, role, name: form.name || "Demo User" });
  };

  return (
    <div className={`min-h-screen flex items-center justify-center p-4 ${dark ? "bg-gray-950" : "bg-linear-to-br from-emerald-50 via-teal-50 to-cyan-50"}`}>
      <motion.div initial={{ opacity: 0, y: 30, scale: 0.96 }} animate={{ opacity: 1, y: 0, scale: 1 }} transition={{ duration: 0.5 }}
        className={`w-full max-w-md rounded-3xl p-8 ${dark ? "bg-gray-900 border border-gray-800" : "bg-white/90 backdrop-blur-md border border-white/60"} shadow-2xl shadow-emerald-200/30`}>

        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 rounded-xl bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center">
            <Leaf size={20} className="text-white" />
          </div>
          <div>
            <div className={`font-extrabold text-lg ${dark ? "text-white" : "text-gray-900"}`}>{t.appName}</div>
            <div className="text-xs text-gray-500">{mode === "login" ? t.signInContinue : t.createAccount}</div>
          </div>
        </div>

        {/* Role selector */}
        <div className="mb-6">
          <label className={`block text-xs font-bold mb-2 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.role}</label>
          <div className="grid grid-cols-3 gap-2">
            {[["farmer", t.farmer, "🌾"], ["vet", t.vet, "🩺"], ["admin", t.admin, "⚙️"]].map(([r, label, icon]) => (
              <button key={r} onClick={() => setRole(r)}
                className={`py-2.5 rounded-xl text-sm font-semibold transition-all border ${role === r ? "bg-emerald-500 text-white border-emerald-500 shadow-lg shadow-emerald-500/30" : dark ? "bg-gray-800 text-gray-300 border-gray-700 hover:border-emerald-400" : "bg-gray-50 text-gray-600 border-gray-200 hover:border-emerald-300"}`}>
                {icon} {label}
              </button>
            ))}
          </div>
        </div>

        <div className="space-y-4">
          {mode === "register" && (
            <div>
              <label className={`block text-xs font-bold mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.name}</label>
              <input value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} placeholder="Ravi Kumar"
                className={`w-full px-4 py-3 rounded-xl border text-sm outline-none focus:ring-2 focus:ring-emerald-400 transition-all ${dark ? "bg-gray-800 border-gray-700 text-white placeholder-gray-500" : "bg-white border-gray-200 text-gray-900 placeholder-gray-400"}`} />
            </div>
          )}
          <div>
            <label className={`block text-xs font-bold mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.email}</label>
            <input type="email" value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} placeholder="farmer@example.com"
              className={`w-full px-4 py-3 rounded-xl border text-sm outline-none focus:ring-2 focus:ring-emerald-400 transition-all ${dark ? "bg-gray-800 border-gray-700 text-white placeholder-gray-500" : "bg-white border-gray-200 text-gray-900 placeholder-gray-400"}`} />
          </div>
          <div>
            <label className={`block text-xs font-bold mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.password}</label>
            <input type="password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} placeholder="••••••••"
              className={`w-full px-4 py-3 rounded-xl border text-sm outline-none focus:ring-2 focus:ring-emerald-400 transition-all ${dark ? "bg-gray-800 border-gray-700 text-white placeholder-gray-500" : "bg-white border-gray-200 text-gray-900 placeholder-gray-400"}`} />
          </div>
        </div>

        <GradientBtn onClick={handleSubmit} className="w-full mt-6 py-3 text-base" disabled={loading}>
          {loading ? (
            <span className="flex items-center justify-center gap-2">
              <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 0.8, ease: "linear" }}
                className="w-4 h-4 rounded-full border-2 border-white/30 border-t-white" />
              Processing...
            </span>
          ) : mode === "login" ? t.login : t.register}
        </GradientBtn>

        <p className={`text-center text-sm mt-4 ${dark ? "text-gray-400" : "text-gray-500"}`}>
          {mode === "login" ? t.noAccount : t.alreadyAccount}{" "}
          <button onClick={onToggle} className="text-emerald-600 font-semibold hover:underline">
            {mode === "login" ? t.register : t.login}
          </button>
        </p>
      </motion.div>
    </div>
  );
};

// ─── EMERGENCY MODAL ───────────────────────────────────────────────────────────
const EmergencyModal = ({ disease, onDismiss, lang, dark }) => {
  const t = T[lang];
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
      <motion.div initial={{ scale: 0.8, y: 40 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.8, y: 40 }}
        className={`w-full max-w-md rounded-3xl overflow-hidden shadow-2xl ${dark ? "bg-gray-900" : "bg-white"}`}>
        {/* Red header */}
        <div className="bg-linear-to-r from-red-500 to-rose-600 p-6 relative overflow-hidden">
          <motion.div animate={{ scale: [1, 1.2, 1] }} transition={{ repeat: Infinity, duration: 1.5 }}
            className="absolute -top-4 -right-4 w-20 h-20 rounded-full bg-red-400/30" />
          <div className="flex items-center gap-3 mb-2">
            <motion.div animate={{ rotate: [-10, 10, -10] }} transition={{ repeat: Infinity, duration: 0.5 }}>
              <AlertTriangle size={28} className="text-white" />
            </motion.div>
            <h2 className="text-xl font-extrabold text-white">{t.emergency}</h2>
          </div>
          <p className="text-red-100 text-sm">{disease.name} — Severity: {disease.severity}</p>
        </div>
        <div className="p-6">
          <div className="mb-4">
            <div className={`text-sm font-bold mb-2 ${dark ? "text-white" : "text-gray-800"}`}>🚨 Immediate Actions Required:</div>
            {disease.firstAid.slice(0, 3).map((step, i) => (
              <div key={i} className="flex items-start gap-2 mb-2">
                <div className="w-5 h-5 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">{i + 1}</div>
                <span className={`text-sm ${dark ? "text-gray-300" : "text-gray-600"}`}>{step}</span>
              </div>
            ))}
          </div>
          <div className="flex gap-3">
            <GradientBtn variant="danger" onClick={() => {}} className="flex-1 flex items-center justify-center gap-2">
              <Phone size={16} /> {t.callVet}
            </GradientBtn>
            <button onClick={onDismiss} className={`px-4 py-2.5 rounded-xl border text-sm font-medium ${dark ? "border-gray-700 text-gray-400 hover:bg-gray-800" : "border-gray-200 text-gray-600 hover:bg-gray-50"}`}>
              {t.dismiss}
            </button>
          </div>
        </div>
      </motion.div>
    </motion.div>
  );
};

// ─── SIDEBAR ───────────────────────────────────────────────────────────────────
const Sidebar = ({ active, onNav, user, collapsed, onCollapse, lang, dark, unreadCount }) => {
  const t = T[lang];
  const navItems = [
    { key: "dashboard", icon: Home, label: t.dashboard },
    { key: "animals", icon: Heart, label: t.animals },
    { key: "diagnosis", icon: Camera, label: t.diagnosis },
    { key: "notifications", icon: Bell, label: t.notifications, badge: unreadCount },
    { key: "reports", icon: BarChart2, label: t.reports },
    { key: "voice", icon: Mic, label: t.voiceAssistant },
    { key: "settings", icon: Settings, label: t.settings },
  ];

  return (
    <motion.aside animate={{ width: collapsed ? 72 : 240 }} transition={{ duration: 0.3 }}
      className={`fixed left-0 top-0 h-full z-30 flex flex-col border-r ${dark ? "bg-gray-900 border-gray-800" : "bg-white border-gray-100"} shadow-xl`}>
      {/* Logo */}
      <div className="h-16 flex items-center px-4 border-b gap-3 border-gray-100 dark:border-gray-800">
        <div className="w-9 h-9 rounded-xl bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center shrink-0 shadow-lg">
          <Leaf size={18} className="text-white" />
        </div>
        {!collapsed && <span className={`font-extrabold text-base truncate ${dark ? "text-white" : "text-gray-900"}`}>{t.appName}</span>}
        <button onClick={onCollapse} className={`ml-auto p-1.5 rounded-lg ${dark ? "hover:bg-gray-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}>
          {collapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
        </button>
      </div>

      {/* User */}
      {!collapsed && (
        <div className={`mx-3 mt-3 p-3 rounded-xl ${dark ? "bg-gray-800" : "bg-emerald-50"}`}>
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-full bg-linear-to-br from-emerald-400 to-teal-500 flex items-center justify-center text-white font-bold text-sm shrink-0">
              {(user?.name || "U")[0]}
            </div>
            <div className="min-w-0">
              <div className={`text-sm font-bold truncate ${dark ? "text-white" : "text-gray-900"}`}>{user?.name || "Demo User"}</div>
              <div className="text-xs text-emerald-600 capitalize">{user?.role || "farmer"}</div>
            </div>
          </div>
        </div>
      )}

      {/* Nav */}
      <nav className="flex-1 px-3 py-4 space-y-1 overflow-y-auto">
        {navItems.map(item => (
          <motion.button key={item.key} whileHover={{ x: 2 }} onClick={() => onNav(item.key)}
            className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all relative
              ${active === item.key
                ? "bg-linear-to-r from-emerald-500 to-teal-500 text-white shadow-lg shadow-emerald-500/25"
                : dark ? "text-gray-400 hover:bg-gray-800 hover:text-white" : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"}`}>
            <item.icon size={18} className="shrink-0" />
            {!collapsed && <span className="truncate">{item.label}</span>}
            {item.badge > 0 && (
              <span className={`${collapsed ? "absolute -top-1 -right-1" : "ml-auto"} min-w-[18px] h-[18px] px-1 rounded-full bg-red-500 text-white text-[10px] font-bold flex items-center justify-center`}>
                {item.badge}
              </span>
            )}
          </motion.button>
        ))}
      </nav>

      {/* Logout */}
      <div className="p-3 border-t border-gray-100 dark:border-gray-800">
        <button className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium ${dark ? "text-gray-400 hover:bg-gray-800 hover:text-red-400" : "text-gray-600 hover:bg-red-50 hover:text-red-600"} transition-all`}>
          <LogOut size={18} className="shrink-0" />
          {!collapsed && <span>{t.logout}</span>}
        </button>
      </div>
    </motion.aside>
  );
};

// ─── DASHBOARD ─────────────────────────────────────────────────────────────────
const Dashboard = ({ lang, dark, addToast }) => {
  const t = T[lang];
  const stats = [
    { label: t.totalAnimals, value: 24, icon: Heart, color: "emerald", delta: "+3" },
    { label: t.healthAlerts, value: 4, icon: AlertTriangle, color: "red", delta: "-1" },
    { label: t.recentDiagnoses, value: 12, icon: Stethoscope, color: "blue", delta: "+5" },
    { label: t.activeVets, value: 8, icon: Users, color: "violet", delta: "+2" },
  ];

  const colorMap = { emerald: "from-emerald-500 to-teal-500 shadow-emerald-500/25", red: "from-red-500 to-rose-500 shadow-red-500/25", blue: "from-blue-500 to-indigo-500 shadow-blue-500/25", violet: "from-violet-500 to-purple-500 shadow-violet-500/25" };

  return (
    <div className="space-y-6">
      <div>
        <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.dashboard}</h1>
        <p className={`text-sm mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>Farm overview — {new Date().toLocaleDateString("en-IN", { weekday: "long", year: "numeric", month: "long", day: "numeric" })}</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((s, i) => (
          <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.1 }}
            className={`p-5 rounded-2xl border ${dark ? "bg-gray-800 border-gray-700" : "bg-white border-gray-100"} shadow-sm`}>
            <div className={`w-10 h-10 rounded-xl bg-linear-to-br ${colorMap[s.color]} flex items-center justify-center mb-3 shadow-lg`}>
              <s.icon size={18} className="text-white" />
            </div>
            <div className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{s.value}</div>
            <div className={`text-xs mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{s.label}</div>
            <div className={`text-xs font-semibold mt-1 ${s.delta.startsWith("+") ? "text-emerald-600" : "text-red-500"}`}>{s.delta} this week</div>
          </motion.div>
        ))}
      </div>

      {/* Charts row */}
      <div className="grid lg:grid-cols-2 gap-6">
        <GlassCard dark={dark} className="p-5">
          <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Health Trend (6 Months)</h3>
          <ResponsiveContainer width="100%" height={200}>
            <AreaChart data={HEALTH_TREND}>
              <defs>
                <linearGradient id="healthyGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#10b981" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#10b981" stopOpacity={0} />
                </linearGradient>
                <linearGradient id="sickGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#f59e0b" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke={dark ? "#374151" : "#f3f4f6"} />
              <XAxis dataKey="month" tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
              <YAxis tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
              <Tooltip contentStyle={{ background: dark ? "#1f2937" : "#fff", border: "none", borderRadius: 12, fontSize: 12 }} />
              <Area type="monotone" dataKey="healthy" stroke="#10b981" fill="url(#healthyGrad)" strokeWidth={2} name="Healthy" />
              <Area type="monotone" dataKey="sick" stroke="#f59e0b" fill="url(#sickGrad)" strokeWidth={2} name="Sick" />
            </AreaChart>
          </ResponsiveContainer>
        </GlassCard>

        <GlassCard dark={dark} className="p-5">
          <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Disease Distribution</h3>
          <div className="flex items-center gap-4">
            <ResponsiveContainer width="60%" height={180}>
              <PieChart>
                <Pie data={DISEASE_DISTRIBUTION} cx="50%" cy="50%" innerRadius={50} outerRadius={80} paddingAngle={3} dataKey="value">
                  {DISEASE_DISTRIBUTION.map((entry, i) => <Cell key={i} fill={entry.color} />)}
                </Pie>
                <Tooltip contentStyle={{ background: dark ? "#1f2937" : "#fff", border: "none", borderRadius: 12, fontSize: 11 }} />
              </PieChart>
            </ResponsiveContainer>
            <div className="flex-1 space-y-2">
              {DISEASE_DISTRIBUTION.map((d, i) => (
                <div key={i} className="flex items-center gap-2 text-xs">
                  <div className="w-2.5 h-2.5 rounded-full shrink-0" style={{ background: d.color }} />
                  <span className={dark ? "text-gray-300" : "text-gray-600"}>{d.name}</span>
                  <span className="ml-auto font-bold" style={{ color: d.color }}>{d.value}%</span>
                </div>
              ))}
            </div>
          </div>
        </GlassCard>
      </div>

      {/* Weight trend */}
      <GlassCard dark={dark} className="p-5">
        <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Average Weight Trend</h3>
        <ResponsiveContainer width="100%" height={180}>
          <BarChart data={WEIGHT_TREND}>
            <CartesianGrid strokeDasharray="3 3" stroke={dark ? "#374151" : "#f3f4f6"} />
            <XAxis dataKey="week" tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
            <YAxis tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
            <Tooltip contentStyle={{ background: dark ? "#1f2937" : "#fff", border: "none", borderRadius: 12, fontSize: 12 }} />
            <Legend iconType="circle" iconSize={8} />
            <Bar dataKey="cow" fill="#10b981" radius={[6, 6, 0, 0]} name="Cow (kg)" />
            <Bar dataKey="goat" fill="#3b82f6" radius={[6, 6, 0, 0]} name="Goat (kg)" />
            <Bar dataKey="sheep" fill="#8b5cf6" radius={[6, 6, 0, 0]} name="Sheep (kg)" />
          </BarChart>
        </ResponsiveContainer>
      </GlassCard>

      {/* Recent alerts */}
      <GlassCard dark={dark} className="p-5">
        <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Recent Animals</h3>
        <div className="space-y-3">
          {MOCK_ANIMALS.slice(0, 4).map(a => (
            <div key={a.id} className={`flex items-center gap-3 p-3 rounded-xl ${dark ? "bg-gray-800/60" : "bg-gray-50"}`}>
              <span className="text-2xl">{a.image}</span>
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2">
                  <span className={`font-semibold text-sm ${dark ? "text-white" : "text-gray-900"}`}>{a.name}</span>
                  <StatusDot status={a.status} />
                </div>
                <div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{a.breed} • {a.type}</div>
              </div>
              <div className="text-right">
                <div className={`text-sm font-bold ${a.healthScore >= 80 ? "text-emerald-600" : a.healthScore >= 60 ? "text-amber-600" : "text-red-600"}`}>{a.healthScore}%</div>
                <div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>Health</div>
              </div>
            </div>
          ))}
        </div>
      </GlassCard>
    </div>
  );
};

// ─── AI DIAGNOSIS ──────────────────────────────────────────────────────────────
const DiagnosisPage = ({ lang, dark, addToast, onEmergency }) => {
  const t = T[lang];
  const [dragOver, setDragOver] = useState(false);
  const [uploaded, setUploaded] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [selectedAnimal, setSelectedAnimal] = useState("Cow");
  const fileRef = useRef();

  const handleAnalyze = async () => {
    setLoading(true);
    await new Promise(r => setTimeout(r, 2500));
    const filtered = DISEASES.filter(d => d.animal === selectedAnimal);
    const disease = filtered[Math.floor(Math.random() * filtered.length)] || DISEASES[0];
    setResult(disease);
    setLoading(false);
    addToast("Analysis complete!", "success");
    if (disease.severity === "Critical") {
      setTimeout(() => onEmergency(disease), 500);
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.diagnosis}</h1>
        <p className={`text-sm mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>Upload a photo for instant AI-powered disease detection</p>
      </div>

      {/* Animal selector */}
      <GlassCard dark={dark} className="p-5">
        <div className={`text-sm font-bold mb-3 ${dark ? "text-gray-300" : "text-gray-700"}`}>Select Animal Type</div>
        <div className="flex gap-3 flex-wrap">
          {[["Cow", "🐄"], ["Goat", "🐐"], ["Sheep", "🐑"]].map(([type, emoji]) => (
            <button key={type} onClick={() => setSelectedAnimal(type)}
              className={`flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold border transition-all ${selectedAnimal === type ? "bg-emerald-500 text-white border-emerald-500 shadow-lg shadow-emerald-500/30" : dark ? "bg-gray-800 text-gray-300 border-gray-700 hover:border-emerald-400" : "bg-white text-gray-600 border-gray-200 hover:border-emerald-300"}`}>
              <span className="text-lg">{emoji}</span> {type}
            </button>
          ))}
        </div>
      </GlassCard>

      {/* Upload area */}
      <GlassCard dark={dark} className="p-5">
        <div
          onDragOver={e => { e.preventDefault(); setDragOver(true); }}
          onDragLeave={() => setDragOver(false)}
          onDrop={e => { e.preventDefault(); setDragOver(false); setUploaded(true); addToast("Image uploaded!", "success"); }}
          onClick={() => fileRef.current?.click()}
          className={`border-2 border-dashed rounded-2xl p-10 text-center cursor-pointer transition-all ${dragOver ? "border-emerald-400 bg-emerald-50" : dark ? "border-gray-700 hover:border-emerald-500 bg-gray-800/40" : "border-gray-200 hover:border-emerald-400 bg-gray-50/50"}`}>
          <input ref={fileRef} type="file" accept="image/*,.heic,.heif,.webp,.bmp" className="hidden" onChange={() => { setUploaded(true); addToast("Image uploaded!", "success"); }} />
          <AnimatePresence mode="wait">
            {uploaded ? (
              <motion.div key="uploaded" initial={{ scale: 0 }} animate={{ scale: 1 }} className="flex flex-col items-center gap-3">
                <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center">
                  <Check size={32} className="text-emerald-600" />
                </div>
                <div className={`font-semibold ${dark ? "text-white" : "text-gray-900"}`}>Image Ready for Analysis</div>
                <div className="text-xs text-emerald-600">animal_photo.jpg</div>
              </motion.div>
            ) : (
              <motion.div key="upload" className="flex flex-col items-center gap-3">
                <div className={`w-16 h-16 rounded-2xl ${dark ? "bg-gray-700" : "bg-gray-100"} flex items-center justify-center`}>
                  <Upload size={28} className="text-gray-400" />
                </div>
                <div className={`font-semibold ${dark ? "text-white" : "text-gray-700"}`}>{t.uploadImage}</div>
                <div className={`text-xs ${dark ? "text-gray-500" : "text-gray-400"}`}>Drag & drop or click to upload • JPG, PNG, HEIC</div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        <div className="mt-4 flex gap-3">
          <GradientBtn onClick={handleAnalyze} disabled={!uploaded || loading} className="flex-1 flex items-center justify-center gap-2 py-3">
            {loading ? (
              <>
                <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 0.8, ease: "linear" }} className="w-4 h-4 rounded-full border-2 border-white/30 border-t-white" />
                Analyzing...
              </>
            ) : (
              <><Activity size={16} /> {t.analyzeDisease}</>
            )}
          </GradientBtn>
          {uploaded && <button onClick={() => { setUploaded(false); setResult(null); }} className={`px-4 rounded-xl border text-sm ${dark ? "border-gray-700 text-gray-400" : "border-gray-200 text-gray-500"} hover:opacity-70`}><RefreshCw size={16} /></button>}
        </div>
      </GlassCard>

      {/* Loading */}
      <AnimatePresence>
        {loading && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
            <GlassCard dark={dark} className="p-6">
              <div className="flex items-center gap-4 mb-4">
                <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1.5, ease: "linear" }}
                  className="w-12 h-12 rounded-full border-4 border-emerald-200 border-t-emerald-600" />
                <div>
                  <div className={`font-bold ${dark ? "text-white" : "text-gray-900"}`}>AI Analyzing Image...</div>
                  <div className="text-xs text-emerald-600">Running deep learning models</div>
                </div>
              </div>
              {["Preprocessing image", "Detecting features", "Running disease classifier", "Generating report"].map((step, i) => (
                <motion.div key={i} initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.4 }}
                  className="flex items-center gap-3 mb-2 text-sm">
                  <motion.div animate={{ opacity: [0.3, 1, 0.3] }} transition={{ repeat: Infinity, duration: 1.5, delay: i * 0.3 }}
                    className="w-2 h-2 rounded-full bg-emerald-500" />
                  <span className={dark ? "text-gray-300" : "text-gray-600"}>{step}</span>
                </motion.div>
              ))}
            </GlassCard>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Result */}
      <AnimatePresence>
        {result && !loading && (
          <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}>
            <GlassCard dark={dark} className="overflow-hidden">
              {/* Result header */}
              <div className={`p-5 border-b ${dark ? "border-gray-700 bg-gray-800/60" : "border-gray-100 bg-linear-to-r from-emerald-50 to-teal-50"}`}>
                <div className="flex items-start justify-between mb-3">
                  <div>
                    <div className={`text-xs font-bold uppercase tracking-wider mb-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.diseaseDetected}</div>
                    <h2 className={`text-xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{result.name}</h2>
                  </div>
                  <SeverityBadge level={result.severity} />
                </div>
                <div className="flex items-center gap-3">
                  <span className={`text-sm ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.confidence}</span>
                  <div className="flex-1 h-3 rounded-full bg-gray-100 dark:bg-gray-700 overflow-hidden">
                    <motion.div initial={{ width: 0 }} animate={{ width: `${result.confidence}%` }} transition={{ duration: 1.2, ease: "easeOut" }}
                      className={`h-full rounded-full bg-linear-to-r ${result.confidence > 85 ? "from-emerald-400 to-emerald-600" : "from-amber-400 to-amber-600"}`} />
                  </div>
                  <span className={`text-sm font-extrabold ${result.confidence > 85 ? "text-emerald-600" : "text-amber-600"}`}>{result.confidence}%</span>
                </div>
              </div>

              <div className="p-5 grid md:grid-cols-2 gap-5">
                {/* Symptoms */}
                <div>
                  <h3 className={`font-bold text-sm mb-3 flex items-center gap-2 ${dark ? "text-white" : "text-gray-900"}`}>
                    <Thermometer size={16} className="text-red-500" /> {t.symptoms}
                  </h3>
                  <ul className="space-y-1.5">
                    {result.symptoms.map((s, i) => (
                      <li key={i} className="flex items-center gap-2 text-sm">
                        <div className="w-1.5 h-1.5 rounded-full bg-red-400 shrink-0" />
                        <span className={dark ? "text-gray-300" : "text-gray-600"}>{s}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Causes */}
                <div>
                  <h3 className={`font-bold text-sm mb-3 flex items-center gap-2 ${dark ? "text-white" : "text-gray-900"}`}>
                    <Wind size={16} className="text-amber-500" /> {t.causes}
                  </h3>
                  <ul className="space-y-1.5">
                    {result.causes.map((c, i) => (
                      <li key={i} className="flex items-center gap-2 text-sm">
                        <div className="w-1.5 h-1.5 rounded-full bg-amber-400 shrink-0" />
                        <span className={dark ? "text-gray-300" : "text-gray-600"}>{c}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Prevention */}
                <div>
                  <h3 className={`font-bold text-sm mb-3 flex items-center gap-2 ${dark ? "text-white" : "text-gray-900"}`}>
                    <Shield size={16} className="text-emerald-500" /> {t.prevention}
                  </h3>
                  <ul className="space-y-1.5">
                    {result.prevention.map((p, i) => (
                      <li key={i} className="flex items-center gap-2 text-sm">
                        <Check size={12} className="text-emerald-500 shrink-0" />
                        <span className={dark ? "text-gray-300" : "text-gray-600"}>{p}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* First Aid */}
                <div>
                  <h3 className={`font-bold text-sm mb-3 flex items-center gap-2 ${dark ? "text-white" : "text-gray-900"}`}>
                    <Heart size={16} className="text-pink-500" /> {t.firstAid}
                  </h3>
                  <ul className="space-y-1.5">
                    {result.firstAid.map((f, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm">
                        <span className="w-4 h-4 rounded-full bg-pink-100 text-pink-600 text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">{i + 1}</span>
                        <span className={dark ? "text-gray-300" : "text-gray-600"}>{f}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              {result.severity === "Critical" && (
                <div className="mx-5 mb-5 p-4 rounded-xl bg-red-50 border border-red-200 flex items-center gap-3">
                  <AlertTriangle size={20} className="text-red-500 shrink-0" />
                  <div className="flex-1">
                    <div className="text-sm font-bold text-red-700">Critical Severity — Immediate Action Required</div>
                    <div className="text-xs text-red-600 mt-0.5">Contact your veterinarian immediately. Do not wait.</div>
                  </div>
                  <GradientBtn variant="danger" onClick={() => onEmergency(result)} className="shrink-0">
                    <Phone size={14} />
                  </GradientBtn>
                </div>
              )}
            </GlassCard>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

// ─── ANIMALS PAGE ──────────────────────────────────────────────────────────────
const AnimalsPage = ({ lang, dark, addToast }) => {
  const t = T[lang];
  const [animals, setAnimals] = useState(MOCK_ANIMALS);
  const [filter, setFilter] = useState("All");
  const [search, setSearch] = useState("");
  const [showAdd, setShowAdd] = useState(false);
  const [newAnimal, setNewAnimal] = useState({ name: "", type: "Cow", breed: "", age: "", weight: "" });

  const filtered = animals.filter(a =>
    (filter === "All" || a.type === filter || a.status === filter) &&
    (a.name.toLowerCase().includes(search.toLowerCase()) || a.breed.toLowerCase().includes(search.toLowerCase()))
  );

  const addAnimal = () => {
    if (!newAnimal.name || !newAnimal.breed) { addToast("Please fill all fields", "error"); return; }
    const newA = {
      id: `${newAnimal.type[0]}${String(animals.length + 1).padStart(3, "0")}`,
      ...newAnimal, age: parseInt(newAnimal.age) || 1, weight: parseInt(newAnimal.weight) || 50,
      status: "Healthy", healthScore: 90, lastCheckup: new Date().toISOString().split("T")[0],
      vaccineStatus: "upToDate",
      image: newAnimal.type === "Cow" ? "🐄" : newAnimal.type === "Goat" ? "🐐" : "🐑"
    };
    setAnimals([...animals, newA]);
    setShowAdd(false);
    setNewAnimal({ name: "", type: "Cow", breed: "", age: "", weight: "" });
    addToast("Animal added successfully!", "success");
  };

  const statusColor = { Healthy: "text-emerald-600", Sick: "text-amber-600", Critical: "text-red-600" };
  const vaccineColor = { upToDate: "text-emerald-600 bg-emerald-50", due: "text-amber-600 bg-amber-50", overdue: "text-red-600 bg-red-50" };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between flex-wrap gap-4">
        <div>
          <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.animals}</h1>
          <p className={`text-sm mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{animals.length} animals registered</p>
        </div>
        <GradientBtn onClick={() => setShowAdd(true)} className="flex items-center gap-2">
          <PlusCircle size={16} /> {t.addAnimal}
        </GradientBtn>
      </div>

      {/* Filters */}
      <GlassCard dark={dark} className="p-4 flex flex-wrap gap-3">
        <div className={`flex items-center gap-2 flex-1 min-w-48 px-3 py-2.5 rounded-xl border ${dark ? "bg-gray-800 border-gray-700" : "bg-white border-gray-200"}`}>
          <Search size={16} className="text-gray-400" />
          <input value={search} onChange={e => setSearch(e.target.value)} placeholder="Search animals..."
            className={`flex-1 text-sm bg-transparent outline-none ${dark ? "text-white placeholder-gray-500" : "text-gray-900 placeholder-gray-400"}`} />
        </div>
        <div className="flex gap-2 flex-wrap">
          {["All", "Cow", "Goat", "Sheep", "Healthy", "Sick", "Critical"].map(f => (
            <button key={f} onClick={() => setFilter(f)}
              className={`px-3 py-2 rounded-xl text-xs font-semibold transition-all border ${filter === f ? "bg-emerald-500 text-white border-emerald-500" : dark ? "bg-gray-800 text-gray-400 border-gray-700 hover:border-emerald-400" : "bg-white text-gray-600 border-gray-200 hover:border-emerald-300"}`}>
              {f}
            </button>
          ))}
        </div>
      </GlassCard>

      {/* Animal grid */}
      <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-4">
        {filtered.map((a, i) => (
          <motion.div key={a.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.07 }} layout>
            <GlassCard dark={dark} className="p-5">
              <div className="flex items-start gap-3 mb-4">
                <div className={`w-14 h-14 rounded-2xl flex items-center justify-center text-3xl ${dark ? "bg-gray-700" : "bg-gray-100"} shrink-0`}>
                  {a.image}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <span className={`font-bold truncate ${dark ? "text-white" : "text-gray-900"}`}>{a.name}</span>
                    <StatusDot status={a.status} />
                  </div>
                  <div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{a.id} • {a.breed}</div>
                  <div className={`text-xs mt-1 font-semibold ${statusColor[a.status]}`}>{a.status}</div>
                </div>
                <div className="text-right">
                  <div className={`text-xl font-extrabold ${a.healthScore >= 80 ? "text-emerald-600" : a.healthScore >= 60 ? "text-amber-600" : "text-red-600"}`}>{a.healthScore}</div>
                  <div className={`text-[10px] ${dark ? "text-gray-500" : "text-gray-400"}`}>score</div>
                </div>
              </div>

              {/* Health bar */}
              <div className="mb-4">
                <div className={`flex justify-between text-xs mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>
                  <span>{t.healthScore}</span><span>{a.healthScore}%</span>
                </div>
                <div className="h-2 rounded-full bg-gray-100 dark:bg-gray-700 overflow-hidden">
                  <div className={`h-full rounded-full ${a.healthScore >= 80 ? "bg-emerald-500" : a.healthScore >= 60 ? "bg-amber-500" : "bg-red-500"}`} style={{ width: `${a.healthScore}%` }} />
                </div>
              </div>

              <div className="grid grid-cols-3 gap-2 text-center text-xs mb-4">
                <div className={`p-2 rounded-xl ${dark ? "bg-gray-800" : "bg-gray-50"}`}>
                  <div className={`font-bold ${dark ? "text-white" : "text-gray-900"}`}>{a.age}y</div>
                  <div className={dark ? "text-gray-500" : "text-gray-400"}>{t.age}</div>
                </div>
                <div className={`p-2 rounded-xl ${dark ? "bg-gray-800" : "bg-gray-50"}`}>
                  <div className={`font-bold ${dark ? "text-white" : "text-gray-900"}`}>{a.weight}</div>
                  <div className={dark ? "text-gray-500" : "text-gray-400"}>kg</div>
                </div>
                <div className={`p-2 rounded-xl ${vaccineColor[a.vaccineStatus]}`}>
                  <div className="font-bold text-[10px]">{t[a.vaccineStatus] || a.vaccineStatus}</div>
                  <div className="text-[10px]">Vaccine</div>
                </div>
              </div>

              <div className={`text-xs ${dark ? "text-gray-500" : "text-gray-400"} flex items-center gap-1`}>
                <Clock size={10} /> Last checkup: {a.lastCheckup}
              </div>
            </GlassCard>
          </motion.div>
        ))}
      </div>

      {/* Add Modal */}
      <AnimatePresence>
        {showAdd && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-40 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm"
            onClick={e => e.target === e.currentTarget && setShowAdd(false)}>
            <motion.div initial={{ scale: 0.9, y: 20 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.9 }}
              className={`w-full max-w-md rounded-2xl p-6 ${dark ? "bg-gray-900 border border-gray-800" : "bg-white"} shadow-2xl`}>
              <div className="flex justify-between items-center mb-5">
                <h3 className={`font-bold text-lg ${dark ? "text-white" : "text-gray-900"}`}>{t.addAnimal}</h3>
                <button onClick={() => setShowAdd(false)} className={`p-2 rounded-lg ${dark ? "hover:bg-gray-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}><X size={18} /></button>
              </div>
              <div className="space-y-4">
                {[["name", t.animalId, "e.g. Lakshmi"], ["breed", t.breed, "e.g. Holstein Friesian"], ["age", t.age, "e.g. 3"], ["weight", t.weight, "e.g. 480"]].map(([k, label, ph]) => (
                  <div key={k}>
                    <label className={`block text-xs font-bold mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{label}</label>
                    <input value={newAnimal[k]} onChange={e => setNewAnimal({ ...newAnimal, [k]: e.target.value })} placeholder={ph}
                      className={`w-full px-4 py-3 rounded-xl border text-sm outline-none focus:ring-2 focus:ring-emerald-400 ${dark ? "bg-gray-800 border-gray-700 text-white" : "bg-white border-gray-200 text-gray-900"}`} />
                  </div>
                ))}
                <div>
                  <label className={`block text-xs font-bold mb-1.5 ${dark ? "text-gray-400" : "text-gray-500"}`}>Type</label>
                  <div className="flex gap-2">
                    {["Cow", "Goat", "Sheep"].map(type => (
                      <button key={type} onClick={() => setNewAnimal({ ...newAnimal, type })}
                        className={`flex-1 py-2.5 rounded-xl text-sm font-semibold border transition-all ${newAnimal.type === type ? "bg-emerald-500 text-white border-emerald-500" : dark ? "bg-gray-800 text-gray-300 border-gray-700" : "bg-gray-50 text-gray-600 border-gray-200"}`}>
                        {type === "Cow" ? "🐄" : type === "Goat" ? "🐐" : "🐑"} {type}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
              <div className="flex gap-3 mt-6">
                <GradientBtn onClick={addAnimal} className="flex-1">Save Animal</GradientBtn>
                <button onClick={() => setShowAdd(false)} className={`px-4 py-2.5 rounded-xl border text-sm ${dark ? "border-gray-700 text-gray-400" : "border-gray-200 text-gray-500"}`}>Cancel</button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

// ─── NOTIFICATIONS PAGE ────────────────────────────────────────────────────────
const NotificationsPage = ({ lang, dark }) => {
  const t = T[lang];
  const [notes, setNotes] = useState(NOTIFICATIONS);
  const iconMap = { critical: <AlertTriangle size={16} className="text-red-500" />, warning: <Bell size={16} className="text-amber-500" />, info: <Info size={16} className="text-blue-500" />, success: <CheckCircle size={16} className="text-emerald-500" /> };
  const bgMap = { critical: dark ? "border-red-500/30 bg-red-500/5" : "border-red-100 bg-red-50/50", warning: dark ? "border-amber-500/30 bg-amber-500/5" : "border-amber-100 bg-amber-50/50", info: dark ? "border-blue-500/30 bg-blue-500/5" : "border-blue-50", success: dark ? "border-emerald-500/30 bg-emerald-500/5" : "border-emerald-100 bg-emerald-50/50" };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.notifications}</h1>
          <p className={`text-sm mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{notes.filter(n => !n.read).length} unread</p>
        </div>
        <button onClick={() => setNotes(notes.map(n => ({ ...n, read: true })))}
          className={`text-sm font-medium text-emerald-600 hover:underline`}>Mark all read</button>
      </div>
      <div className="space-y-3">
        {notes.map((n, i) => (
          <motion.div key={n.id} initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: i * 0.07 }}
            onClick={() => setNotes(notes.map(nn => nn.id === n.id ? { ...nn, read: true } : nn))}
            className={`p-4 rounded-2xl border cursor-pointer transition-all hover:scale-[1.01] ${bgMap[n.type]} ${!n.read ? "ring-1 ring-offset-0" : ""} ${n.type === "critical" && !n.read ? "ring-red-300" : ""}`}>
            <div className="flex items-start gap-3">
              <div className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 ${n.type === "critical" ? "bg-red-100" : n.type === "warning" ? "bg-amber-100" : n.type === "success" ? "bg-emerald-100" : "bg-blue-100"}`}>
                {iconMap[n.type]}
              </div>
              <div className="flex-1 min-w-0">
                <div className={`font-semibold text-sm ${dark ? "text-white" : "text-gray-900"} ${!n.read ? "font-bold" : ""}`}>{n.title}</div>
                <div className={`text-xs mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{n.body}</div>
              </div>
              <div className="flex items-center gap-2 shrink-0">
                <span className={`text-xs ${dark ? "text-gray-500" : "text-gray-400"}`}>{n.time}</span>
                {!n.read && <div className="w-2 h-2 rounded-full bg-emerald-500" />}
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
};

// ─── REPORTS PAGE ──────────────────────────────────────────────────────────────
const ReportsPage = ({ lang, dark }) => {
  const t = T[lang];
  return (
    <div className="space-y-6">
      <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.reports}</h1>
      <div className="grid md:grid-cols-2 gap-6">
        <GlassCard dark={dark} className="p-5">
          <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Monthly Diagnoses</h3>
          <ResponsiveContainer width="100%" height={200}>
            <LineChart data={HEALTH_TREND}>
              <CartesianGrid strokeDasharray="3 3" stroke={dark ? "#374151" : "#f3f4f6"} />
              <XAxis dataKey="month" tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
              <YAxis tick={{ fontSize: 11, fill: dark ? "#9ca3af" : "#6b7280" }} />
              <Tooltip contentStyle={{ background: dark ? "#1f2937" : "#fff", border: "none", borderRadius: 12 }} />
              <Line type="monotone" dataKey="healthy" stroke="#10b981" strokeWidth={3} dot={{ fill: "#10b981", r: 4 }} name="Healthy" />
              <Line type="monotone" dataKey="sick" stroke="#f59e0b" strokeWidth={3} dot={{ fill: "#f59e0b", r: 4 }} name="Sick" />
              <Line type="monotone" dataKey="critical" stroke="#ef4444" strokeWidth={3} dot={{ fill: "#ef4444", r: 4 }} name="Critical" />
            </LineChart>
          </ResponsiveContainer>
        </GlassCard>

        <GlassCard dark={dark} className="p-5">
          <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Top Diseases This Month</h3>
          <div className="space-y-3">
            {DISEASE_DISTRIBUTION.map((d, i) => (
              <div key={i}>
                <div className={`flex justify-between text-sm mb-1 ${dark ? "text-gray-300" : "text-gray-700"}`}>
                  <span>{d.name}</span><span className="font-bold">{d.value}%</span>
                </div>
                <div className={`h-2.5 rounded-full ${dark ? "bg-gray-700" : "bg-gray-100"} overflow-hidden`}>
                  <motion.div initial={{ width: 0 }} animate={{ width: `${d.value}%` }} transition={{ delay: i * 0.15, duration: 0.8 }}
                    className="h-full rounded-full" style={{ background: d.color }} />
                </div>
              </div>
            ))}
          </div>
        </GlassCard>
      </div>

      {/* Summary table */}
      <GlassCard dark={dark} className="p-5">
        <h3 className={`font-bold mb-4 ${dark ? "text-white" : "text-gray-900"}`}>Animal Health Summary</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className={`text-xs font-bold uppercase tracking-wider ${dark ? "text-gray-400" : "text-gray-500"}`}>
                <th className="text-left py-2 pr-4">Animal</th>
                <th className="text-left py-2 pr-4">Type</th>
                <th className="text-left py-2 pr-4">Status</th>
                <th className="text-left py-2 pr-4">Health</th>
                <th className="text-left py-2">Last Check</th>
              </tr>
            </thead>
            <tbody>
              {MOCK_ANIMALS.map(a => (
                <tr key={a.id} className={`border-t ${dark ? "border-gray-800" : "border-gray-100"}`}>
                  <td className={`py-3 pr-4 font-medium ${dark ? "text-white" : "text-gray-900"}`}>{a.image} {a.name}</td>
                  <td className={`py-3 pr-4 ${dark ? "text-gray-400" : "text-gray-500"}`}>{a.type}</td>
                  <td className="py-3 pr-4"><StatusDot status={a.status} /> <span className={`ml-1.5 text-xs ${a.status === "Healthy" ? "text-emerald-600" : a.status === "Sick" ? "text-amber-600" : "text-red-600"}`}>{a.status}</span></td>
                  <td className="py-3 pr-4">
                    <div className="flex items-center gap-2">
                      <div className={`w-16 h-1.5 rounded-full ${dark ? "bg-gray-700" : "bg-gray-100"} overflow-hidden`}>
                        <div className={`h-full rounded-full ${a.healthScore >= 80 ? "bg-emerald-500" : a.healthScore >= 60 ? "bg-amber-500" : "bg-red-500"}`} style={{ width: `${a.healthScore}%` }} />
                      </div>
                      <span className={`text-xs font-bold ${a.healthScore >= 80 ? "text-emerald-600" : a.healthScore >= 60 ? "text-amber-600" : "text-red-600"}`}>{a.healthScore}%</span>
                    </div>
                  </td>
                  <td className={`py-3 text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{a.lastCheckup}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </GlassCard>
    </div>
  );
};

// ─── VOICE ASSISTANT ───────────────────────────────────────────────────────────
const VoicePage = ({ lang, dark }) => {
  const t = T[lang];
  const [listening, setListening] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [response, setResponse] = useState("");
  const [history, setHistory] = useState([
    { role: "assistant", text: "Hello! I'm your livestock health assistant. Ask me about animal diseases, symptoms, or health tips." }
  ]);

  const questions = ["What are symptoms of FMD?", "How to prevent Mastitis?", "My cow has fever, what to do?", "Best vaccine schedule for goats?"];

  const handleListen = async () => {
    setListening(true);
    await new Promise(r => setTimeout(r, 2000));
    const q = questions[Math.floor(Math.random() * questions.length)];
    setTranscript(q);
    setListening(false);
    await new Promise(r => setTimeout(r, 500));
    setHistory(h => [...h, { role: "user", text: q }]);
    await new Promise(r => setTimeout(r, 1000));
    const answers = {
      "What are symptoms of FMD?": "Foot and Mouth Disease symptoms include: high fever above 40°C, blisters on mouth and hooves, excessive drooling, lameness, and loss of appetite. Isolate the animal immediately and contact your vet.",
      "How to prevent Mastitis?": "To prevent Mastitis: always pre and post-dip teats after milking, maintain clean dry bedding, perform regular udder checks, and consider dry cow therapy at the end of lactation.",
      "My cow has fever, what to do?": "First, measure the exact temperature. Normal cow temp is 38–39.5°C. If above 40°C, isolate the cow, ensure fresh water access, and call your veterinarian immediately. Do not administer medication without vet guidance.",
      "Best vaccine schedule for goats?": "For goats: Enterotoxemia vaccine at 4-6 weeks, booster at 3 weeks later. Goat Pox annually before monsoon. FMD every 6 months. PPR vaccine annually. Keep records of all vaccinations."
    };
    setHistory(h => [...h, { role: "assistant", text: answers[q] || "I can help you with that. Please consult your veterinarian for accurate diagnosis." }]);
    setTranscript("");
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.voiceAssistant}</h1>
        <p className={`text-sm mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>Ask anything about livestock health in your language</p>
      </div>

      {/* Chat */}
      <GlassCard dark={dark} className="p-5">
        <div className="space-y-4 max-h-72 overflow-y-auto mb-5 pr-1">
          {history.map((m, i) => (
            <motion.div key={i} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}
              className={`flex gap-3 ${m.role === "user" ? "justify-end" : ""}`}>
              {m.role === "assistant" && (
                <div className="w-8 h-8 rounded-full bg-linear-to-br from-emerald-500 to-teal-500 flex items-center justify-center shrink-0">
                  <Leaf size={14} className="text-white" />
                </div>
              )}
              <div className={`max-w-[80%] px-4 py-3 rounded-2xl text-sm ${m.role === "user"
                ? "bg-linear-to-r from-emerald-500 to-teal-500 text-white rounded-tr-sm"
                : dark ? "bg-gray-800 text-gray-300 rounded-tl-sm" : "bg-gray-100 text-gray-700 rounded-tl-sm"}`}>
                {m.text}
              </div>
            </motion.div>
          ))}
          {transcript && (
            <div className="flex justify-end">
              <div className="px-4 py-3 rounded-2xl bg-emerald-100 text-emerald-800 text-sm italic">{transcript}</div>
            </div>
          )}
        </div>

        {/* Mic button */}
        <div className="flex flex-col items-center gap-4">
          <motion.button onClick={handleListen} disabled={listening}
            whileTap={{ scale: 0.95 }}
            className={`relative w-20 h-20 rounded-full flex items-center justify-center shadow-xl transition-all
              ${listening ? "bg-red-500 shadow-red-500/40" : "bg-linear-to-br from-emerald-500 to-teal-500 shadow-emerald-500/40"}`}>
            {listening && (
              <motion.div animate={{ scale: [1, 1.4, 1] }} transition={{ repeat: Infinity, duration: 1.5 }}
                className="absolute inset-0 rounded-full bg-emerald-400/30" />
            )}
            {listening ? <MicOff size={28} className="text-white relative z-10" /> : <Mic size={28} className="text-white relative z-10" />}
          </motion.button>
          <div className={`text-sm font-medium ${dark ? "text-gray-300" : "text-gray-600"}`}>
            {listening ? <span className="text-red-500 flex items-center gap-2"><motion.div animate={{ opacity: [1, 0] }} transition={{ repeat: Infinity, duration: 0.8 }} className="w-2 h-2 rounded-full bg-red-500" />{t.speaking}</span> : "Tap to ask"}
          </div>
        </div>
      </GlassCard>

      {/* Quick questions */}
      <GlassCard dark={dark} className="p-5">
        <div className={`text-sm font-bold mb-3 ${dark ? "text-gray-300" : "text-gray-700"}`}>Quick Questions</div>
        <div className="flex flex-wrap gap-2">
          {questions.map((q, i) => (
            <button key={i} onClick={() => {
              setHistory(h => [...h, { role: "user", text: q }, { role: "assistant", text: "Let me look that up for you. Based on our AI knowledge base, " + q.split("?")[0].toLowerCase() + " is an important topic for livestock health. Please consult a veterinarian for personalized advice." }]);
            }}
              className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all ${dark ? "bg-gray-800 border-gray-700 text-gray-300 hover:border-emerald-400 hover:text-emerald-400" : "bg-white border-gray-200 text-gray-600 hover:border-emerald-400 hover:text-emerald-600"}`}>
              {q}
            </button>
          ))}
        </div>
      </GlassCard>
    </div>
  );
};

// ─── SETTINGS PAGE ─────────────────────────────────────────────────────────────
const SettingsPage = ({ lang, setLang, dark, setDark }) => {
  const t = T[lang];
  return (
    <div className="space-y-6">
      <h1 className={`text-2xl font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{t.settings}</h1>

      <GlassCard dark={dark} className="p-5 space-y-5">
        {/* Language */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Globe size={20} className="text-emerald-500" />
            <div>
              <div className={`font-semibold text-sm ${dark ? "text-white" : "text-gray-900"}`}>{t.language}</div>
              <div className="text-xs text-gray-500">App display language</div>
            </div>
          </div>
          <div className="flex gap-2">
            {[["en", "EN"], ["kn", "ಕ"], ["hi", "हि"]].map(([code, label]) => (
              <button key={code} onClick={() => setLang(code)}
                className={`w-10 h-10 rounded-xl text-sm font-bold transition-all ${lang === code ? "bg-emerald-500 text-white shadow-lg shadow-emerald-500/30" : dark ? "bg-gray-800 text-gray-400 hover:bg-gray-700" : "bg-gray-100 text-gray-600 hover:bg-gray-200"}`}>
                {label}
              </button>
            ))}
          </div>
        </div>

        <div className={`border-t ${dark ? "border-gray-700" : "border-gray-100"}`} />

        {/* Dark mode */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            {dark ? <Moon size={20} className="text-emerald-500" /> : <Sun size={20} className="text-emerald-500" />}
            <div>
              <div className={`font-semibold text-sm ${dark ? "text-white" : "text-gray-900"}`}>{t.darkMode}</div>
              <div className="text-xs text-gray-500">Switch theme</div>
            </div>
          </div>
          <button onClick={() => setDark(!dark)}
            className={`relative w-12 h-6 rounded-full transition-all ${dark ? "bg-emerald-500" : "bg-gray-200"}`}>
            <motion.div animate={{ x: dark ? 24 : 2 }} transition={{ type: "spring", stiffness: 300, damping: 30 }}
              className="absolute top-1 w-4 h-4 rounded-full bg-white shadow-md" />
          </button>
        </div>

        <div className={`border-t ${dark ? "border-gray-700" : "border-gray-100"}`} />

        {/* Notifications */}
        {[["Push Notifications", "Get alerts for critical health events", true], ["Email Reports", "Weekly health summary via email", true], ["SMS Alerts", "Emergency SMS notifications", false]].map(([title, desc, active], i) => (
          <div key={i} className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Bell size={20} className="text-emerald-500" />
              <div>
                <div className={`font-semibold text-sm ${dark ? "text-white" : "text-gray-900"}`}>{title}</div>
                <div className="text-xs text-gray-500">{desc}</div>
              </div>
            </div>
            <div className={`w-10 h-5 rounded-full ${active ? "bg-emerald-500" : dark ? "bg-gray-700" : "bg-gray-200"} relative`}>
              <div className={`absolute top-0.5 w-4 h-4 rounded-full bg-white shadow transition-all ${active ? "left-5" : "left-0.5"}`} />
            </div>
          </div>
        ))}
      </GlassCard>

      {/* Profile card */}
      <GlassCard dark={dark} className="p-5">
        <div className={`text-sm font-bold mb-4 ${dark ? "text-gray-300" : "text-gray-700"}`}>Account</div>
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 rounded-2xl bg-linear-to-br from-emerald-400 to-teal-500 flex items-center justify-center text-white font-extrabold text-2xl">R</div>
          <div>
            <div className={`font-bold ${dark ? "text-white" : "text-gray-900"}`}>Ravi Kumar</div>
            <div className="text-sm text-emerald-600">Farmer • Karnataka</div>
            <div className="text-xs text-gray-500">ravi@farm.example.com</div>
          </div>
        </div>
        <div className="grid grid-cols-3 gap-3 text-center">
          {[["24", "Animals"], ["156", "Diagnoses"], ["4.9★", "Rating"]].map(([v, l]) => (
            <div key={l} className={`p-3 rounded-xl ${dark ? "bg-gray-800" : "bg-gray-50"}`}>
              <div className={`font-extrabold ${dark ? "text-white" : "text-gray-900"}`}>{v}</div>
              <div className="text-xs text-gray-500">{l}</div>
            </div>
          ))}
        </div>
      </GlassCard>
    </div>
  );
};

// ─── MAIN APP ──────────────────────────────────────────────────────────────────
export default function App() {
  const [page, setPage] = useState("landing");
  const [authMode, setAuthMode] = useState("login");
  const [user, setUser] = useState(null);
  const [dark, setDark] = useState(false);
  const [lang, setLang] = useState("en");
  const [activeNav, setActiveNav] = useState("dashboard");
  const [collapsed, setCollapsed] = useState(false);
  const [emergency, setEmergency] = useState(null);
  const [toasts, setToasts] = useState([]);

  const addToast = useCallback((message, type = "info") => {
    const id = Date.now();
    setToasts(t => [...t, { id, message, type }]);
    setTimeout(() => setToasts(t => t.filter(tt => tt.id !== id)), 4000);
  }, []);

  const removeToast = useCallback(id => setToasts(t => t.filter(tt => tt.id !== id)), []);

  const unreadCount = NOTIFICATIONS.filter(n => !n.read).length;

  const handleAuth = (userData) => {
    setUser(userData);
    setPage("app");
    addToast(`${T[lang].welcomeBack}, ${userData.name}! 🌿`, "success");
  };

  const renderContent = () => {
    const props = { lang, dark, addToast, onEmergency: setEmergency };
    switch (activeNav) {
      case "dashboard": return <Dashboard {...props} />;
      case "animals": return <AnimalsPage {...props} />;
      case "diagnosis": return <DiagnosisPage {...props} />;
      case "notifications": return <NotificationsPage {...props} />;
      case "reports": return <ReportsPage {...props} />;
      case "voice": return <VoicePage {...props} />;
      case "settings": return <SettingsPage lang={lang} setLang={setLang} dark={dark} setDark={setDark} />;
      default: return <Dashboard {...props} />;
    }
  };

  return (
    <div className={dark ? "dark" : ""}>
      <div className={`min-h-screen ${dark ? "bg-gray-950 text-white" : "bg-gray-50 text-gray-900"} transition-colors duration-300`}>
        <AnimatePresence mode="wait">
          {page === "landing" && (
            <motion.div key="landing" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
              <LandingPage onEnter={mode => { setAuthMode(mode); setPage("auth"); }} lang={lang} dark={dark} />
            </motion.div>
          )}

          {page === "auth" && (
            <motion.div key="auth" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
              <AuthPage mode={authMode} onAuth={handleAuth} onToggle={() => setAuthMode(m => m === "login" ? "register" : "login")} lang={lang} dark={dark} />
            </motion.div>
          )}

          {page === "app" && (
            <motion.div key="app" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex">
              <Sidebar active={activeNav} onNav={setActiveNav} user={user} collapsed={collapsed} onCollapse={() => setCollapsed(c => !c)} lang={lang} dark={dark} unreadCount={unreadCount} />

              {/* Main content */}
              <main className={`flex-1 min-h-screen transition-all duration-300 ${collapsed ? "ml-[72px]" : "ml-[240px]"}`}>
                {/* Top bar */}
                <div className={`sticky top-0 z-20 h-16 flex items-center justify-between px-6 border-b backdrop-blur-md ${dark ? "bg-gray-950/90 border-gray-800" : "bg-white/90 border-gray-100"}`}>
                  <div className="flex items-center gap-3">
                    <button onClick={() => setCollapsed(c => !c)} className={`p-2 rounded-lg ${dark ? "hover:bg-gray-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"} md:hidden`}>
                      <Menu size={20} />
                    </button>
                    <div>
                      <div className={`text-sm font-bold capitalize ${dark ? "text-white" : "text-gray-900"}`}>{T[lang][activeNav] || activeNav}</div>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    {/* Lang toggle */}
                    <div className="flex gap-1">
                      {[["en", "EN"], ["kn", "ಕ"], ["hi", "हि"]].map(([c, l]) => (
                        <button key={c} onClick={() => setLang(c)}
                          className={`w-8 h-8 rounded-lg text-xs font-bold transition-all ${lang === c ? "bg-emerald-500 text-white" : dark ? "text-gray-400 hover:bg-gray-800" : "text-gray-500 hover:bg-gray-100"}`}>{l}</button>
                      ))}
                    </div>
                    <button onClick={() => setDark(d => !d)} className={`p-2 rounded-lg ${dark ? "hover:bg-gray-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}>
                      {dark ? <Sun size={18} /> : <Moon size={18} />}
                    </button>
                    <button onClick={() => setActiveNav("notifications")} className={`relative p-2 rounded-lg ${dark ? "hover:bg-gray-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}>
                      <Bell size={18} />
                      {unreadCount > 0 && <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-red-500 animate-pulse" />}
                    </button>
                    <div className="w-8 h-8 rounded-full bg-linear-to-br from-emerald-400 to-teal-500 flex items-center justify-center text-white text-xs font-bold">
                      {(user?.name || "U")[0]}
                    </div>
                  </div>
                </div>

                <div className="p-6 max-w-5xl mx-auto">
                  <AnimatePresence mode="wait">
                    <motion.div key={activeNav} initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }} transition={{ duration: 0.3 }}>
                      {renderContent()}
                    </motion.div>
                  </AnimatePresence>
                </div>
              </main>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Emergency modal */}
        <AnimatePresence>
          {emergency && (
            <EmergencyModal disease={emergency} onDismiss={() => setEmergency(null)} lang={lang} dark={dark} />
          )}
        </AnimatePresence>

        {/* Toasts */}
        <Toast toasts={toasts} removeToast={removeToast} />
      </div>
    </div>
  );
}

