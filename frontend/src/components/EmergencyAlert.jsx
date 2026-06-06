import React, { useState, useEffect } from "react";
import { AlertOctagon, Phone, X, AlertTriangle, MapPin, Search, ArrowLeft } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useLanguage } from "../context/LanguageContext";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const EmergencyAlert = ({ isOpen, onClose, diseaseName, severity, firstAid = [] }) => {
  const { t } = useLanguage();
  const navigate = useNavigate();

  // Tab views: 'alert' (main alert details), 'call' (vet details panel)
  const [view, setView] = useState("alert");
  
  // Geolocation & Vet lookup states
  const [loadingVet, setLoadingVet] = useState(false);
  const [locDenied, setLocDenied] = useState(false);
  const [locError, setLocError] = useState("");
  const [nearestVet, setNearestVet] = useState(null);

  // Manual search form fields
  const [district, setDistrict] = useState("");
  const [village, setVillage] = useState("");
  const [pincode, setPincode] = useState("");

  // Reset states when modal closes/opens
  useEffect(() => {
    if (isOpen) {
      setView("alert");
      setNearestVet(null);
      setLocDenied(false);
      setLocError("");
      setDistrict("");
      setVillage("");
      setPincode("");
    }
  }, [isOpen]);

  const handleEmergencyCallClick = () => {
    setView("call");
    getUserLocationAndFetchVet();
  };

  const getUserLocationAndFetchVet = () => {
    if (!navigator.geolocation) {
      setLocError(t("unableToAccessLocation"));
      setLocDenied(true);
      return;
    }

    setLoadingVet(true);
    setLocError("");
    setLocDenied(false);

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const { latitude, longitude } = position.coords;
        await fetchNearestVet(latitude, longitude);
      },
      (err) => {
        console.warn("Geolocation permission denied or error:", err);
        setLocError(t("unableToAccessLocation"));
        setLocDenied(true);
        setLoadingVet(false);
      },
      { timeout: 10000 }
    );
  };

  const fetchNearestVet = async (lat, lng) => {
    setLoadingVet(true);
    try {
      const response = await api.get("/api/vets/nearby", {
        params: { lat, lng }
      });
      const results = response.data.results || [];
      if (results.length > 0) {
        setNearestVet(results[0]); // First returned element is the nearest
      } else {
        setNearestVet(null);
        setLocError(t("noVetsFound"));
      }
    } catch (err) {
      console.error("Error fetching nearby vets:", err);
      setLocError(t("fetchVetsError"));
    } finally {
      setLoadingVet(false);
    }
  };

  const handleManualSearch = async (e) => {
    e.preventDefault();
    if (!district && !village && !pincode) return;

    setLoadingVet(true);
    setLocError("");
    try {
      const response = await api.get("/api/vets/search-address", {
        params: { district, village, pincode }
      });
      
      if (response.data.success) {
        const { lat, lng } = response.data;
        await fetchNearestVet(lat, lng);
      } else {
        setLocError(response.data.error || t("noVetsFound"));
        setLoadingVet(false);
      }
    } catch (err) {
      console.error("Manual address search failed:", err);
      setLocError(t("fetchVetsError"));
      setLoadingVet(false);
    }
  };

  const handleViewNearbyHospitalsClick = () => {
    onClose();
    navigate("/vets");
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
          <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 20 }}
            transition={{ duration: 0.3, ease: "easeOut" }}
            className="w-full max-w-xl bg-slate-900 border border-red-500/40 rounded-2xl overflow-hidden shadow-2xl shadow-red-900/30"
          >
            {/* Header banner */}
            <div className="bg-linear-to-r from-red-700 to-rose-800 p-6 text-slate-50 relative">
              <button
                onClick={onClose}
                className="absolute top-4 right-4 p-2 rounded-full hover:bg-white/10 text-white/80 hover:text-white transition-colors cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
              
              <div className="flex items-center space-x-3">
                <AlertOctagon className="w-8 h-8 text-slate-50 animate-bounce" />
                <div>
                  <h2 className="text-xl font-extrabold tracking-wide uppercase">
                    {t("emergencyDiseaseAlert")}
                  </h2>
                  <p className="text-xs text-red-100/90 font-medium mt-0.5">
                    {t("diseaseName")}: <span className="font-extrabold">{diseaseName}</span>
                  </p>
                </div>
              </div>
            </div>

            {/* Content view toggle */}
            <div className="p-6 space-y-5 max-h-[75vh] overflow-y-auto custom-scrollbar">
              {view === "alert" ? (
                <>
                  {/* Alert warning box */}
                  <div className="bg-red-500/10 border border-red-500/25 rounded-xl p-4 space-y-2">
                    <div className="flex items-center space-x-2 text-red-400 font-extrabold">
                      <AlertTriangle className="w-5 h-5 shrink-0" />
                      <span className="text-sm uppercase tracking-wider">
                        {t("severity")}: {severity || "HIGH"}
                      </span>
                    </div>
                    <p className="text-sm text-red-200 leading-relaxed font-medium">
                      {t("emergencyAlertText")}
                    </p>
                  </div>

                  {/* First Aid Steps */}
                  {firstAid && firstAid.length > 0 && (
                    <div className="space-y-2.5">
                      <h3 className="text-sm font-extrabold text-slate-200 uppercase tracking-wider">
                        {t("firstAid")} (Immediate Steps):
                      </h3>
                      <ul className="space-y-2">
                        {firstAid.map((step, idx) => (
                          <li key={idx} className="flex items-start space-x-2.5 text-sm text-slate-300">
                            <span className="text-red-400 font-extrabold shrink-0 mt-0.5">{idx + 1}.</span>
                            <span className="leading-relaxed">{step}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Actions buttons */}
                  <div className="pt-4 flex flex-col sm:flex-row gap-3">
                    <button
                      onClick={handleEmergencyCallClick}
                      className="flex-1 flex items-center justify-center space-x-2 bg-red-600 hover:bg-red-750 text-white font-extrabold py-3.5 px-4 rounded-xl shadow-lg shadow-red-600/20 transition cursor-pointer"
                    >
                      <Phone className="w-5 h-5" />
                      <span>{t("emergencyCall")}</span>
                    </button>
                    
                    <button
                      onClick={handleViewNearbyHospitalsClick}
                      className="flex-1 flex items-center justify-center space-x-2 bg-slate-800 hover:bg-slate-750 text-emerald-450 border border-slate-750 font-bold py-3.5 px-4 rounded-xl transition cursor-pointer"
                    >
                      <MapPin className="w-5 h-5" />
                      <span>{t("viewNearbyHospitals")}</span>
                    </button>
                  </div>
                  
                  <div className="text-center pt-2">
                    <button
                      onClick={onClose}
                      className="text-xs text-slate-450 hover:text-slate-300 underline font-medium cursor-pointer"
                    >
                      {t("cancel")}
                    </button>
                  </div>
                </>
              ) : (
                /* Emergency Veterinary Information Panel */
                <div className="space-y-5">
                  <button
                    onClick={() => setView("alert")}
                    className="flex items-center space-x-1.5 text-xs text-slate-400 hover:text-slate-200 transition cursor-pointer font-bold uppercase tracking-wider"
                  >
                    <ArrowLeft className="w-4 h-4" />
                    <span>Back to Alert Details</span>
                  </button>

                  <h3 className="text-base font-extrabold text-slate-200">
                    Emergency Veterinary Support
                  </h3>

                  {loadingVet ? (
                    <div className="flex flex-col items-center justify-center py-10 space-y-3">
                      <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-red-500" />
                      <span className="text-sm text-slate-400">Locating Nearest Clinic...</span>
                    </div>
                  ) : nearestVet ? (
                    <div className="bg-slate-950 border border-slate-800 p-5 rounded-xl space-y-4 shadow-inner">
                      <div className="flex items-start justify-between">
                        <div>
                          <span className="inline-block bg-red-500/10 border border-red-500/25 px-2 py-0.5 rounded text-[10px] text-red-400 font-extrabold uppercase tracking-wide mb-2">
                            Nearest Hospital Found
                          </span>
                          <h4 className="font-extrabold text-slate-100 text-lg leading-tight">
                            {nearestVet.name}
                          </h4>
                          <p className="text-slate-400 text-sm mt-1 flex items-start space-x-1.5">
                            <MapPin className="w-4 h-4 text-red-500 shrink-0 mt-0.5" />
                            <span>{nearestVet.address}</span>
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center space-x-3 text-sm text-slate-350 bg-slate-900 px-4 py-2.5 rounded-lg border border-slate-850">
                        <span className="font-extrabold text-emerald-450 uppercase text-xs tracking-wider">Distance:</span>
                        <span className="font-extrabold text-slate-200">{nearestVet.distance} away</span>
                      </div>

                      {nearestVet.phone ? (
                        <div className="pt-2">
                          <a
                            href={`tel:${nearestVet.phone}`}
                            className="w-full flex items-center justify-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold py-3.5 px-4 rounded-xl shadow-lg shadow-emerald-600/25 transition text-center cursor-pointer"
                          >
                            <Phone className="w-5 h-5 animate-pulse" />
                            <span>Call Hospital ({nearestVet.phone})</span>
                          </a>
                        </div>
                      ) : (
                        <div className="pt-2">
                          <a
                            href="tel:1962"
                            className="w-full flex items-center justify-center space-x-2 bg-red-600 hover:bg-red-700 text-white font-extrabold py-3.5 px-4 rounded-xl shadow-lg shadow-red-600/25 transition text-center cursor-pointer"
                          >
                            <Phone className="w-5 h-5" />
                            <span>Call Emergency Helpline (1962)</span>
                          </a>
                          <p className="text-[11px] text-slate-550 text-center mt-2">
                            No specific hospital number available. Calling government helpdesk instead.
                          </p>
                        </div>
                      )}
                    </div>
                  ) : null}

                  {/* Geolocation Denied / Address Fallback */}
                  {locDenied && (
                    <div className="space-y-4">
                      <div className="bg-amber-500/10 border border-amber-500/25 rounded-xl p-4 space-y-2">
                        <div className="flex items-center space-x-2 text-amber-400 font-extrabold text-sm">
                          <AlertTriangle className="w-4 h-4 shrink-0" />
                          <span>{t("unableToAccessLocation")}</span>
                        </div>
                        <p className="text-xs text-amber-350 leading-relaxed font-medium">
                          Please enter your village, district, or pincode manually to find the closest veterinary facilities.
                        </p>
                      </div>

                      <form onSubmit={handleManualSearch} className="space-y-3.5">
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                          <div>
                            <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
                              {t("village")}
                            </label>
                            <input
                              type="text"
                              value={village}
                              onChange={(e) => setVillage(e.target.value)}
                              placeholder="e.g. Channapatna"
                              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-red-500/50"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
                              {t("district")}
                            </label>
                            <input
                              type="text"
                              value={district}
                              onChange={(e) => setDistrict(e.target.value)}
                              placeholder="e.g. Ramanagara"
                              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-red-500/50"
                            />
                          </div>
                        </div>

                        <div>
                          <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
                            {t("pincode")}
                          </label>
                          <input
                            type="text"
                            value={pincode}
                            onChange={(e) => setPincode(e.target.value)}
                            placeholder="e.g. 562160"
                            className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-red-500/50"
                          />
                        </div>

                        <button
                          type="submit"
                          disabled={loadingVet || (!district && !village && !pincode)}
                          className="w-full py-3.5 bg-red-600 hover:bg-red-750 disabled:bg-slate-800 disabled:text-slate-500 disabled:cursor-not-allowed text-white font-extrabold rounded-xl transition flex items-center justify-center space-x-2 cursor-pointer shadow-lg shadow-red-950/20"
                        >
                          <Search className="w-5 h-5" />
                          <span>{loadingVet ? "Searching..." : t("manualSearchBtn")}</span>
                        </button>
                      </form>
                    </div>
                  )}

                  {locError && !nearestVet && (
                    <div className="bg-red-500/10 border border-red-500/20 rounded-xl p-3 text-red-400 text-xs font-medium text-center">
                      {locError}
                    </div>
                  )}

                  <div className="flex justify-between items-center pt-2">
                    {locDenied && (
                      <button
                        onClick={getUserLocationAndFetchVet}
                        className="text-xs text-emerald-450 hover:text-emerald-400 hover:underline font-bold transition cursor-pointer"
                      >
                        Retry Auto-location
                      </button>
                    )}
                    <button
                      onClick={onClose}
                      className="text-xs text-slate-450 hover:text-slate-300 font-bold transition cursor-pointer ml-auto"
                    >
                      Dismiss Alert
                    </button>
                  </div>
                </div>
              )}
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};

export default EmergencyAlert;

