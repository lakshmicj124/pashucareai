import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLanguage } from "../context/LanguageContext";
import api from "../services/api";
import { 
  Activity, ShieldAlert, CheckCircle, MapPin, MessageSquare, 
  Settings, User, Plus, Calendar, ArrowRight, TrendingUp, Info
} from "lucide-react";
import { motion } from "framer-motion";

const Dashboard = () => {
  const { user } = useAuth();
  const { t, language } = useLanguage();
  const navigate = useNavigate();

  const [detections, setDetections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [location, setLocation] = useState({ lat: 12.9716, lng: 77.5946 }); // Default Bangalore
  const [loadingLoc, setLoadingLoc] = useState(false);

  useEffect(() => {
    fetchDashboardData();
    getUserLocation();
  }, [language]);

  const fetchDashboardData = async () => {
    setLoading(true);
    try {
      const response = await api.get(`/api/detections?lang=${language}`);
      setDetections(response.data || []);
    } catch (err) {
      console.error("Failed to load dashboard predictions history:", err);
    } finally {
      setLoading(false);
    }
  };

  const getUserLocation = () => {
    if (!navigator.geolocation) return;
    setLoadingLoc(true);
    navigator.geolocation.getCurrentPosition(
      (position) => {
        setLocation({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
        setLoadingLoc(false);
      },
      (err) => {
        console.warn("Location check failed. Using fallback coordinates.", err);
        setLoadingLoc(false);
      },
      { timeout: 8000 }
    );
  };

  // Calculate quick stats
  const totalScans = detections.length;
  const healthyCount = detections.filter(d => d.disease_name === "Healthy" || d.disease_name.toLowerCase().includes("healthy")).length;
  const diseasedCount = totalScans - healthyCount;

  const recentPredictions = detections.slice(0, 4);

  const getSeverityBadgeColor = (color) => {
    switch (color) {
      case "red":
        return "bg-red-500/10 border border-red-500/30 text-red-400";
      case "orange":
        return "bg-orange-500/10 border border-orange-500/30 text-orange-400";
      case "amber":
        return "bg-amber-500/10 border border-amber-500/30 text-amber-400";
      default:
        return "bg-green-500/10 border border-green-500/30 text-green-400";
    }
  };

  return (
    <div className="bg-slate-950 text-white min-h-screen py-10 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      {/* Glow blobs */}
      <div className="absolute top-0 right-1/4 w-96 h-96 bg-emerald-500/5 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute bottom-0 left-1/4 w-96 h-96 bg-teal-500/5 rounded-full blur-3xl pointer-events-none"></div>

      <div className="max-w-6xl mx-auto space-y-8 relative z-10">
        
        {/* Welcome Banner */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 shadow-xl">
          <div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white">
              Welcome, <span className="text-transparent bg-clip-text bg-linear-to-r from-emerald-400 to-teal-400">{user?.name || "Farmer"}</span>! 🐄
            </h1>
            <p className="text-slate-400 text-sm mt-1">
              Monitor your livestock health status, run scans, and coordinate with veterinarians.
            </p>
          </div>
          <Link
            to="/detect"
            className="flex items-center space-x-2 px-5 py-3 bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-extrabold rounded-2xl transition shadow-lg shadow-emerald-500/10 cursor-pointer text-sm shrink-0"
          >
            <Plus className="w-5 h-5" />
            <span>Scan Livestock Animal</span>
          </Link>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <motion.div 
            whileHover={{ y: -4 }}
            className="bg-slate-900 border border-slate-850 p-6 rounded-2xl shadow-lg flex items-center space-x-4"
          >
            <div className="w-12 h-12 rounded-xl bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-blue-400">
              <TrendingUp className="w-6 h-6" />
            </div>
            <div>
              <span className="text-xs text-slate-450 uppercase block font-semibold">Total Scans</span>
              <span className="text-2xl font-extrabold text-white">{totalScans}</span>
            </div>
          </motion.div>

          <motion.div 
            whileHover={{ y: -4 }}
            className="bg-slate-900 border border-slate-850 p-6 rounded-2xl shadow-lg flex items-center space-x-4"
          >
            <div className="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
              <CheckCircle className="w-6 h-6" />
            </div>
            <div>
              <span className="text-xs text-slate-450 uppercase block font-semibold">Healthy Animals</span>
              <span className="text-2xl font-extrabold text-emerald-400">{healthyCount}</span>
            </div>
          </motion.div>

          <motion.div 
            whileHover={{ y: -4 }}
            className="bg-slate-900 border border-slate-850 p-6 rounded-2xl shadow-lg flex items-center space-x-4"
          >
            <div className="w-12 h-12 rounded-xl bg-red-500/10 border border-red-500/30 flex items-center justify-center text-red-400">
              <ShieldAlert className="w-6 h-6" />
            </div>
            <div>
              <span className="text-xs text-slate-450 uppercase block font-semibold">Diseases Detected</span>
              <span className="text-2xl font-extrabold text-red-400">{diseasedCount}</span>
            </div>
          </motion.div>
        </div>

        {/* Content Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Left panel: Recent Predictions */}
          <div className="lg:col-span-2 space-y-6">
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
              <div className="flex justify-between items-center border-b border-slate-800 pb-3">
                <h3 className="font-extrabold text-slate-200 flex items-center space-x-2">
                  <Activity className="w-5 h-5 text-emerald-450" />
                  <span>Recent Predictions</span>
                </h3>
                <Link to="/history" className="text-xs font-bold text-emerald-400 hover:underline flex items-center space-x-1">
                  <span>View All</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              </div>

              {loading ? (
                <div className="flex flex-col items-center justify-center py-10 space-y-2">
                  <div className="animate-spin rounded-full h-6 w-6 border-t-2 border-emerald-500" />
                  <span className="text-xs text-slate-500">Loading history logs...</span>
                </div>
              ) : recentPredictions.length === 0 ? (
                <div className="text-center py-12 text-slate-500">
                  <span className="text-3xl block mb-2">📷</span>
                  <p className="text-sm font-semibold">No diagnostic scans conducted yet.</p>
                  <Link to="/detect" className="text-xs text-emerald-400 underline font-bold mt-1 inline-block">
                    Scan your first animal now
                  </Link>
                </div>
              ) : (
                <div className="space-y-4">
                  {recentPredictions.map((record) => (
                    <div 
                      key={record.id}
                      onClick={() => navigate("/history")}
                      className="bg-slate-950/40 border border-slate-850 p-4 rounded-xl flex items-center gap-4 hover:border-slate-750 transition cursor-pointer"
                    >
                      {record.image_url ? (
                        <img 
                          src={`http://127.0.0.1:8000${record.image_url}`} 
                          alt="prediction thumbnail" 
                          className="w-14 h-14 object-cover rounded-lg shrink-0 bg-slate-900"
                        />
                      ) : (
                        <div className="w-14 h-14 rounded-lg bg-slate-900 flex items-center justify-center text-xl shrink-0">
                          {record.animal_type === "Cow" ? "🐄" : record.animal_type === "Goat" ? "🐐" : "🐑"}
                        </div>
                      )}

                      <div className="grow min-w-0">
                        <div className="flex items-center justify-between">
                          <span className="text-[10px] text-slate-500 font-bold uppercase tracking-wider">{record.animal_type}</span>
                          <span className={`px-2 py-0.5 rounded-full text-[9px] font-bold ${getSeverityBadgeColor(record.severity_color)}`}>
                            {record.severity}
                          </span>
                        </div>
                        <h4 className="font-bold text-sm text-slate-200 truncate">{record.disease_name}</h4>
                        <div className="flex justify-between items-center text-[10px] text-slate-500 pt-1">
                          <span className="flex items-center">
                            <Calendar className="w-3 h-3 mr-1" />
                            {new Date(record.timestamp).toLocaleDateString()}
                          </span>
                          <span className="text-emerald-450 font-bold">{record.confidence}% Confidence</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Quick Links Section */}
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
              <h3 className="font-extrabold text-slate-200">Quick Shortcuts</h3>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <Link 
                  to="/chat" 
                  className="bg-slate-950 hover:bg-slate-850 border border-slate-850 hover:border-slate-700 p-4 rounded-2xl text-center space-y-2 transition flex flex-col items-center justify-center cursor-pointer"
                >
                  <MessageSquare className="w-6 h-6 text-emerald-400" />
                  <span className="text-xs font-bold text-slate-350">AI Chatbot</span>
                </Link>

                <Link 
                  to="/vets" 
                  className="bg-slate-950 hover:bg-slate-850 border border-slate-850 hover:border-slate-700 p-4 rounded-2xl text-center space-y-2 transition flex flex-col items-center justify-center cursor-pointer"
                >
                  <MapPin className="w-6 h-6 text-teal-400" />
                  <span className="text-xs font-bold text-slate-350">Find Vets</span>
                </Link>

                <Link 
                  to="/settings" 
                  className="bg-slate-950 hover:bg-slate-850 border border-slate-850 hover:border-slate-700 p-4 rounded-2xl text-center space-y-2 transition flex flex-col items-center justify-center cursor-pointer"
                >
                  <Settings className="w-6 h-6 text-cyan-400" />
                  <span className="text-xs font-bold text-slate-350">Settings</span>
                </Link>

                <Link 
                  to="/history" 
                  className="bg-slate-950 hover:bg-slate-850 border border-slate-850 hover:border-slate-700 p-4 rounded-2xl text-center space-y-2 transition flex flex-col items-center justify-center cursor-pointer"
                >
                  <User className="w-6 h-6 text-blue-400" />
                  <span className="text-xs font-bold text-slate-350">History Logs</span>
                </Link>
              </div>
            </div>
          </div>

          {/* Right panel: Map preview */}
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4 flex flex-col h-full">
              <div className="flex justify-between items-center border-b border-slate-850 pb-3">
                <h3 className="font-extrabold text-slate-200 flex items-center space-x-2">
                  <MapPin className="w-5 h-5 text-emerald-450" />
                  <span>Nearest Vet Map</span>
                </h3>
              </div>

              {/* Mini Map Iframe */}
              <div className="bg-slate-950 border border-slate-850 rounded-2xl overflow-hidden h-64 relative">
                <iframe 
                  src={`https://www.openstreetmap.org/export/embed.html?bbox=${location.lng - 0.03}%2C${location.lat - 0.03}%2C${location.lng + 0.03}%2C${location.lat + 0.03}&layer=mapnik&marker=${location.lat}%2C${location.lng}`}
                  width="100%" 
                  height="100%" 
                  style={{ border: 0 }} 
                  allowFullScreen="" 
                  loading="lazy" 
                  title="Mini OSM Map Preview"
                ></iframe>
              </div>

              <div className="space-y-3 grow flex flex-col justify-end">
                <div className="flex items-start space-x-2 text-xs text-slate-400">
                  <Info className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                  <p>
                    Showing maps of veterinary clinics near your current location. Allow location access for precise local listings.
                  </p>
                </div>
                <Link
                  to="/vets"
                  className="w-full py-3 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 hover:border-emerald-500/50 font-bold rounded-xl transition text-center text-xs block cursor-pointer"
                >
                  Search Nearby Veterinary Clinics
                </Link>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

