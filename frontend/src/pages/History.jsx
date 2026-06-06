import React, { useState, useEffect } from "react";
import { useLanguage } from "../context/LanguageContext";
import { useAuth } from "../context/AuthContext";
import api, { API_BASE_URL } from "../services/api";
import { History as HistoryIcon, Calendar, ArrowRight, ShieldCheck, Clipboard, ExternalLink, Pill, HeartHandshake, Stethoscope, Trash2 } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const History = () => {
  const { t, language } = useLanguage();
  const { user } = useAuth();

  const [detections, setDetections] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [selectedRecord, setSelectedRecord] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, [language]);

  const fetchHistory = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await api.get(`/api/detections?lang=${language}`);
      setDetections(response.data || []);
    } catch (err) {
      console.error(err);
      setError("Could not load detection history. Please check connection.");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id, e) => {
    if (e) e.stopPropagation();
    if (window.confirm("Are you sure you want to delete this diagnosis record?")) {
      try {
        await api.delete(`/api/detections/${id}`);
        setDetections(prev => prev.filter(d => d.id !== id));
        if (selectedRecord?.id === id) {
          setSelectedRecord(null);
        }
      } catch (err) {
        console.error(err);
        setError("Failed to delete the detection record.");
      }
    }
  };

  const filteredDetections = detections.filter(d => 
    (d.disease_name || "").toLowerCase().includes(searchTerm.toLowerCase()) ||
    (d.animal_type || "").toLowerCase().includes(searchTerm.toLowerCase()) ||
    (d.severity || "").toLowerCase().includes(searchTerm.toLowerCase())
  );

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
    <div className="bg-slate-950 text-white min-h-screen py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-transparent bg-clip-text bg-linear-to-r from-emerald-400 to-teal-400">
            {t("historyTitle")}
          </h1>
          <p className="text-slate-400 text-sm max-w-md mx-auto">
            {t("historyDesc")}
          </p>
        </div>

        {error && (
          <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 text-sm">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* List Section */}
          <div className="lg:col-span-1 space-y-4">
            <input
              type="text"
              placeholder="Search history (e.g. Lumpy, Cow, PPR)..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-slate-900 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 placeholder-slate-500"
            />

            {loading ? (
              <div className="flex flex-col items-center justify-center py-20 space-y-3">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-emerald-500" />
                <span className="text-sm text-slate-400">{t("loadingHistory")}</span>
              </div>
            ) : filteredDetections.length === 0 ? (
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 text-center text-slate-450">
                <HistoryIcon className="w-12 h-12 text-slate-600 mx-auto mb-3" />
                <p className="text-sm">No matching records found.</p>
              </div>
            ) : (
              <div className="space-y-4 max-h-[600px] overflow-y-auto pr-2 custom-scrollbar">
                {filteredDetections.map((record) => (
                  <div
                    key={record.id}
                    onClick={() => setSelectedRecord(record)}
                    className={`bg-slate-900 border p-4 rounded-xl space-y-3 cursor-pointer hover:border-slate-700 transition flex items-center gap-4 ${
                      selectedRecord?.id === record.id ? "border-emerald-500 shadow-md shadow-emerald-500/5" : "border-slate-800"
                    }`}
                  >
                    {record.image_url ? (
                      <img
                        src={`${API_BASE_URL}${record.image_url}`}
                        alt="Diagnosis Thumbnail"
                        className="w-16 h-16 rounded-lg object-cover bg-slate-950 shrink-0"
                      />
                    ) : (
                      <div className="w-16 h-16 rounded-lg bg-slate-950 flex items-center justify-center text-2xl shrink-0">
                        {record.animal_type === "Cow" ? "🐄" : record.animal_type === "Goat" ? "🐐" : "🐑"}
                      </div>
                    )}

                    <div className="flex-1 min-w-0 space-y-1">
                      <div className="flex justify-between items-center">
                        <span className="text-xs text-slate-450 font-semibold uppercase tracking-wide">
                          {record.animal_type}
                        </span>
                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${getSeverityBadgeColor(record.severity_color)}`}>
                          {record.severity}
                        </span>
                      </div>
                      <h3 className="font-bold text-slate-200 truncate">{record.disease_name}</h3>
                      <div className="flex justify-between items-center text-[10px] text-slate-400 pt-1">
                        <span className="flex items-center">
                          <Calendar className="w-3 h-3 mr-1" />
                          {new Date(record.timestamp).toLocaleDateString()}
                        </span>
                        <span className="text-emerald-450 font-bold">{record.confidence}% Conf.</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Details Section */}
          <div className="lg:col-span-2">
            <AnimatePresence mode="wait">
              {selectedRecord ? (
                <motion.div
                  key={selectedRecord.id}
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  transition={{ duration: 0.2 }}
                  className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl p-6 space-y-6"
                >
                  <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center border-b border-slate-850 pb-4 gap-4">
                    <div>
                      <span className="text-xs text-emerald-400 font-semibold tracking-widest uppercase">
                        {selectedRecord.animal_type} Diagnostic Report
                      </span>
                      <h2 className="text-2xl font-extrabold text-white mt-1">
                        {selectedRecord.disease_name}
                      </h2>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className={`px-4 py-1.5 rounded-full text-xs font-bold ${getSeverityBadgeColor(selectedRecord.severity_color)}`}>
                        {selectedRecord.severity}
                      </span>
                      <button
                        onClick={(e) => handleDelete(selectedRecord.id, e)}
                        className="bg-red-500/10 hover:bg-red-500/20 text-red-400 p-2 rounded-xl border border-red-500/30 transition cursor-pointer"
                        title="Delete Record"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div className="md:col-span-1 space-y-4">
                      {selectedRecord.image_url && (
                        <div className="border border-slate-850 rounded-xl overflow-hidden bg-slate-950">
                          <img
                            src={`${API_BASE_URL}${selectedRecord.image_url}`}
                            alt="Diagnosis Record"
                            className="w-full h-auto max-h-48 object-contain"
                          />
                        </div>
                      )}
                      <div className="bg-slate-950/45 p-4 rounded-xl border border-slate-850 text-center space-y-1">
                        <span className="text-xs text-slate-450 uppercase block font-semibold">Confidence</span>
                        <span className="text-3xl font-extrabold text-emerald-450">{selectedRecord.confidence}%</span>
                      </div>
                    </div>

                    <div className="md:col-span-2 space-y-6">
                      <div className="space-y-1">
                        <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                          <Clipboard className="w-4 h-4 text-cyan-400" />
                          <span>{t("whyHappened")}</span>
                        </h3>
                        <p className="text-slate-400 text-sm leading-relaxed">
                          {selectedRecord.why_it_happened}
                        </p>
                      </div>

                      <div className="space-y-1">
                        <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                          <HistoryIcon className="w-4 h-4 text-orange-400" />
                          <span>{t("symptoms")}</span>
                        </h3>
                        <ul className="list-disc list-inside text-slate-400 text-sm space-y-0.5">
                          {selectedRecord.symptoms.map((s, idx) => (
                            <li key={idx}>{s}</li>
                          ))}
                        </ul>
                      </div>
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-slate-850">
                    <div className="space-y-2">
                      <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                        <Pill className="w-4 h-4 text-emerald-455" />
                        <span>{t("suggestedMedicine")}</span>
                      </h3>
                      <ul className="list-disc list-inside text-slate-400 text-sm space-y-0.5">
                        {selectedRecord.medicine.map((m, idx) => (
                          <li key={idx}>{m}</li>
                        ))}
                      </ul>
                    </div>

                    <div className="space-y-2">
                      <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                        <ShieldCheck className="w-4 h-4 text-teal-400" />
                        <span>{t("prevention")}</span>
                      </h3>
                      <ul className="list-disc list-inside text-slate-400 text-sm space-y-0.5">
                        {selectedRecord.prevention.map((p, idx) => (
                          <li key={idx}>{p}</li>
                        ))}
                      </ul>
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-slate-850">
                    <div className="space-y-2">
                      <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                        <HeartHandshake className="w-4 h-4 text-emerald-400" />
                        <span>{t("foodRecommendations")}</span>
                      </h3>
                      <ul className="list-disc list-inside text-slate-400 text-sm space-y-0.5">
                        {selectedRecord.food_recommendations.map((f, idx) => (
                          <li key={idx}>{f}</li>
                        ))}
                      </ul>
                    </div>

                    <div className="space-y-2">
                      <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                        <Stethoscope className="w-4 h-4 text-cyan-400" />
                        <span>{t("hygieneSuggestions")}</span>
                      </h3>
                      <ul className="list-disc list-inside text-slate-400 text-sm space-y-0.5">
                        {selectedRecord.hygiene_tips.map((h, idx) => (
                          <li key={idx}>{h}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </motion.div>
              ) : (
                <div className="h-full flex items-center justify-center border border-dashed border-slate-800 rounded-2xl p-12 text-slate-500 min-h-[400px]">
                  <div className="text-center space-y-2">
                    <Clipboard className="w-12 h-12 mx-auto text-slate-700" />
                    <p className="text-sm font-medium">{t("selectHistoryLog")}</p>
                  </div>
                </div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </div>
  );
};

export default History;

