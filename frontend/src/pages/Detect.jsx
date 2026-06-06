import React, { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLanguage } from "../context/LanguageContext";
import api from "../services/api";
import EmergencyAlert from "../components/EmergencyAlert";
import { Upload, Camera, Trash2, ArrowRight, ShieldAlert, HeartHandshake, EyeOff, Activity, ShieldCheck, Pill, Stethoscope, AlertTriangle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const Detect = () => {
  const { user } = useAuth();
  const { t, language } = useLanguage();
  const navigate = useNavigate();

  const [animalType, setAnimalType] = useState("Cow");
  const [image, setImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  // Camera States
  const [cameraActive, setCameraActive] = useState(false);
  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const canvasRef = useRef(null);

  // Emergency Modal
  const [emergencyOpen, setEmergencyOpen] = useState(false);

  // File Change Handler
  const handleFileChange = (e) => {
    setError("");
    const file = e.target.files[0];
    if (file) {
      if (file.size > 10 * 1024 * 1024) {
        setError("File size exceeds 10MB limit.");
        return;
      }
      setImage(file);
      setImagePreview(URL.createObjectURL(file));
      setResult(null);
    }
  };

  // Drag and Drop Handlers
  const [dragActive, setDragActive] = useState(false);
  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    setError("");
    const file = e.dataTransfer.files[0];
    if (file) {
      if (file.size > 10 * 1024 * 1024) {
        setError("File size exceeds 10MB limit.");
        return;
      }
      setImage(file);
      setImagePreview(URL.createObjectURL(file));
      setResult(null);
    }
  };

  // Camera Operations
  const startCamera = async () => {
    setError("");
    setResult(null);
    try {
      setCameraActive(true);
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: "environment" },
      });
      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      }
    } catch (err) {
      console.error(err);
      setError("Could not access camera. Please check permissions.");
      setCameraActive(false);
    }
  };

  const capturePhoto = () => {
    if (videoRef.current && canvasRef.current) {
      const video = videoRef.current;
      const canvas = canvasRef.current;
      const context = canvas.getContext("2d");

      // Set canvas dimensions equal to video stream feed dimensions
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      canvas.toBlob((blob) => {
        const file = new File([blob], "captured_animal.jpg", { type: "image/jpeg" });
        setImage(file);
        setImagePreview(URL.createObjectURL(file));
        stopCamera();
      }, "image/jpeg");
    }
  };

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
      streamRef.current = null;
    }
    setCameraActive(false);
  };

  const removeImage = () => {
    setImage(null);
    setImagePreview(null);
    setResult(null);
    setError("");
  };

  // Submit and Analyze Image
  const handleAnalyze = async () => {
    if (!image) {
      setError("Please select or capture an image first.");
      return;
    }

    if (!user) {
      setError(t("authRequired"));
      navigate("/login");
      return;
    }

    setAnalyzing(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", image);
    formData.append("animal_type", animalType);
    formData.append("lang", language);

    try {
      const response = await api.post("/api/detect", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setResult(response.data);
      if (response.data.severity === "HIGH" || response.data.severity === "CRITICAL" || response.data.severity_color === "red" || response.data.severity_color === "orange") {
        setEmergencyOpen(true);
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "AI analysis failed. Please try again.");
    } finally {
      setAnalyzing(false);
    }
  };

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
      <div className="max-w-4xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-transparent bg-clip-text bg-linear-to-r from-emerald-400 to-teal-400">
            {t("detect")}
          </h1>
          <p className="text-slate-400 text-sm max-w-lg mx-auto">
            {t("detectDesc")}
          </p>
        </div>

        {/* Form Container */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-6 shadow-xl">
          {error && (
            <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 text-sm flex items-center space-x-2">
              <ShieldAlert className="w-5 h-5 shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {/* Animal Tab Selector */}
          <div className="space-y-2">
            <label className="block text-sm font-semibold text-slate-300">
              {t("selectAnimal")}
            </label>
            <div className="grid grid-cols-3 gap-2">
              {["Cow", "Goat", "Sheep"].map((type) => (
                <button
                  key={type}
                  type="button"
                  onClick={() => {
                    setAnimalType(type);
                    removeImage();
                  }}
                  className={`py-3 rounded-xl font-bold transition-all text-sm flex items-center justify-center space-x-2 border cursor-pointer ${
                    animalType === type
                      ? "bg-linear-to-r from-emerald-500 to-teal-500 border-emerald-500 text-slate-950 shadow-md shadow-emerald-500/10"
                      : "bg-slate-950 border-slate-850 text-slate-400 hover:text-white"
                  }`}
                >
                  <span className="text-lg">
                    {type === "Cow" ? "🐄" : type === "Goat" ? "🐐" : "🐑"}
                  </span>
                  <span>{t(type.toLowerCase())}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Image Upload/Capture Section */}
          <div className="space-y-2">
            {!cameraActive && !imagePreview && (
              <div
                onDragEnter={handleDrag}
                onDragOver={handleDrag}
                onDragLeave={handleDrag}
                onDrop={handleDrop}
                className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all flex flex-col items-center justify-center space-y-4 ${
                  dragActive
                    ? "border-emerald-500 bg-emerald-500/5"
                    : "border-slate-800 bg-slate-950 hover:border-slate-700"
                }`}
                onClick={() => document.getElementById("file-input").click()}
              >
                <input
                  id="file-input"
                  type="file"
                  accept="image/*,.heic,.heif,.webp,.bmp"
                  onChange={handleFileChange}
                  className="hidden"
                />
                <div className="p-3 bg-emerald-500/10 rounded-full text-emerald-400">
                  <Upload className="w-8 h-8" />
                </div>
                <div className="space-y-1">
                  <p className="text-sm font-semibold">{t("dragDropText")}</p>
                  <p className="text-xs text-slate-500">{t("supportsFormat")}</p>
                </div>
              </div>
            )}

            {/* Video stream feed */}
            {cameraActive && (
              <div className="relative border border-slate-800 bg-slate-950 rounded-xl overflow-hidden aspect-video flex items-center justify-center">
                <video
                  ref={videoRef}
                  className="w-full h-full object-cover"
                  playsInline
                  muted
                />
                <div className="absolute bottom-4 left-0 right-0 flex justify-center space-x-2 px-4">
                  <button
                    onClick={capturePhoto}
                    className="bg-emerald-500 text-slate-950 font-bold px-4 py-2 rounded-lg text-sm transition hover:bg-emerald-600 cursor-pointer"
                  >
                    {t("capturePhoto")}
                  </button>
                  <button
                    onClick={stopCamera}
                    className="bg-slate-850 border border-slate-700 text-white px-4 py-2 rounded-lg text-sm transition hover:bg-slate-800"
                  >
                    {t("cancel")}
                  </button>
                </div>
              </div>
            )}

            {/* Preview Selected/Captured image */}
            {imagePreview && (
              <div className="relative border border-slate-800 bg-slate-950 rounded-xl p-4 flex flex-col items-center space-y-3">
                <img
                  src={imagePreview}
                  alt="Animal Diagnostics Upload"
                  className="max-h-72 rounded-lg object-contain w-full"
                />
                <div className="flex space-x-2 w-full">
                  <button
                    onClick={removeImage}
                    className="flex-1 flex items-center justify-center space-x-1 py-2 px-4 border border-slate-800 rounded-lg text-sm text-red-400 hover:bg-red-500/10 transition-colors"
                  >
                    <Trash2 className="w-4 h-4" />
                    <span>{t("deleteImage")}</span>
                  </button>
                  <button
                    onClick={startCamera}
                    className="flex-1 flex items-center justify-center space-x-1 py-2 px-4 border border-slate-850 bg-slate-900 rounded-lg text-sm hover:bg-slate-800 transition-colors text-emerald-400"
                  >
                    <Camera className="w-4 h-4" />
                    <span>{t("retakePhoto")}</span>
                  </button>
                </div>
              </div>
            )}

            {/* Trigger camera toggle */}
            {!cameraActive && !imagePreview && (
              <button
                type="button"
                onClick={startCamera}
                className="w-full py-3 bg-slate-950 border border-slate-850 hover:bg-slate-900 rounded-xl text-sm font-semibold flex items-center justify-center space-x-2 text-emerald-400 transition"
              >
                <Camera className="w-5 h-5" />
                <span>{t("cameraCapture")}</span>
              </button>
            )}
          </div>

          <canvas ref={canvasRef} className="hidden" />

          {/* Action Analyze button */}
          <button
            type="button"
            onClick={handleAnalyze}
            disabled={!image || analyzing}
            className="w-full py-4 bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-extrabold text-base rounded-xl transition shadow-lg shadow-emerald-500/20 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-2 cursor-pointer"
          >
            {analyzing ? (
              <>
                <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-slate-950" />
                <span>{t("analyzing")}</span>
              </>
            ) : (
              <>
                <ShieldAlert className="w-5 h-5 shrink-0" />
                <span>{t("analyzeBtn")}</span>
              </>
            )}
          </button>
        </div>

        {/* Results display Section */}
        <AnimatePresence>
          {result && (
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 30 }}
              transition={{ duration: 0.4 }}
              className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl"
            >
              {result.disease_name === "Healthy" ? (
                <div className="p-8 text-center space-y-6">
                  <div className="mx-auto w-20 h-20 bg-green-500/10 border border-green-500/30 rounded-full flex items-center justify-center text-green-400">
                    <ShieldCheck className="w-12 h-12" />
                  </div>
                  <div className="space-y-2">
                    <h2 className="text-3xl font-extrabold text-transparent bg-clip-text bg-linear-to-r from-green-400 to-emerald-400">
                      {t("noVisibleSigns")}
                    </h2>
                    <p className="text-slate-400 text-sm max-w-md mx-auto">
                      {result.why_it_happened || "The animal appears to be in excellent condition. Maintain proper feeding and regular checks."}
                    </p>
                  </div>
                  <div className="bg-slate-950/50 border border-slate-850 rounded-xl p-6 max-w-lg mx-auto text-left space-y-4">
                    <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                      <Activity className="w-4 h-4 text-green-400" />
                      <span>General Health Status</span>
                    </h3>
                    <ul className="text-sm text-slate-400 space-y-2">
                      <li className="flex items-center space-x-2">
                        <span className="w-2 h-2 bg-green-500 rounded-full"></span>
                        <span>Confidence: <strong className="text-green-400">{result.confidence}%</strong></span>
                      </li>
                      {result.symptoms && result.symptoms.map((s, idx) => (
                        <li key={idx} className="flex items-center space-x-2">
                          <span className="w-2 h-2 bg-green-500 rounded-full"></span>
                          <span>{s}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ) : (
                <>
                  {/* Header result */}
                  <div className="bg-slate-850 border-b border-slate-800 p-6 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div className="space-y-1">
                      <span className="text-xs text-emerald-400 font-semibold tracking-widest uppercase">
                        {t("resultTitle")}
                      </span>
                      <h2 className="text-2xl font-extrabold text-white">
                        {result.disease_name}
                      </h2>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className={`px-4 py-1.5 rounded-full text-xs font-bold ${getSeverityBadgeColor(result.severity_color)}`}>
                        {result.severity}
                      </span>
                    </div>
                  </div>

                  {/* Body details */}
                  <div className="p-6 space-y-6">
                    {/* Confidence Bar */}
                    <div className="space-y-2">
                      <div className="flex justify-between items-center text-sm font-semibold">
                        <span className="text-slate-400">{t("confidence")}</span>
                        <span className="text-emerald-450 font-bold">{result.confidence}%</span>
                      </div>
                      <div className="w-full bg-slate-950 rounded-full h-3 overflow-hidden border border-slate-850">
                        <motion.div
                          initial={{ width: 0 }}
                          animate={{ width: `${result.confidence}%` }}
                          transition={{ duration: 0.8, ease: "easeOut" }}
                          className="bg-linear-to-r from-emerald-500 to-teal-500 h-full rounded-full"
                        />
                      </div>
                    </div>

                    {/* Grid details */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4 border-t border-slate-850">
                      {/* Left Column */}
                      <div className="space-y-6">
                        {/* Why it Happened */}
                        <div className="space-y-2">
                          <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                            <Activity className="w-4 h-4 text-cyan-400" />
                            <span>{t("whyHappened")}</span>
                          </h3>
                          <p className="text-slate-400 text-sm leading-relaxed">
                            {result.why_it_happened}
                          </p>
                        </div>

                        {/* Causes */}
                        {result.causes && result.causes.length > 0 && (
                          <div className="space-y-2">
                            <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                              <AlertTriangle className="w-4 h-4 text-amber-500" />
                              <span>{t("causes")}</span>
                            </h3>
                            <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                              {result.causes.map((cause, idx) => (
                                <li key={idx}>{cause}</li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {/* Symptoms */}
                        <div className="space-y-2">
                          <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                            <ShieldAlert className="w-4 h-4 text-orange-400" />
                            <span>{t("symptoms")}</span>
                          </h3>
                          <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                            {result.symptoms.map((symptom, idx) => (
                              <li key={idx}>{symptom}</li>
                            ))}
                          </ul>
                        </div>
                      </div>

                      {/* Right Column */}
                      <div className="space-y-6">
                        {/* Medicines */}
                        <div className="space-y-2">
                          <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                            <Pill className="w-4 h-4 text-emerald-450" />
                            <span>{t("suggestedMedicine")}</span>
                          </h3>
                          <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                            {result.medicine.map((med, idx) => (
                              <li key={idx}>{med}</li>
                            ))}
                          </ul>
                        </div>

                        {/* First Aid */}
                        {result.first_aid && result.first_aid.length > 0 && (
                          <div className="space-y-2">
                            <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                              <HeartHandshake className="w-4 h-4 text-rose-400" />
                              <span>{t("firstAid")}</span>
                            </h3>
                            <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                              {result.first_aid.map((fa, idx) => (
                                <li key={idx}>{fa}</li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {/* Prevention */}
                        <div className="space-y-2">
                          <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                            <ShieldCheck className="w-4 h-4 text-teal-400" />
                            <span>{t("prevention")}</span>
                          </h3>
                          <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                            {result.prevention.map((prev, idx) => (
                              <li key={idx}>{prev}</li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    </div>

                    {/* Additional Guidance details */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-slate-850">
                      {/* Food Guidance */}
                      <div className="space-y-2">
                        <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                          <HeartHandshake className="w-4 h-4 text-emerald-400" />
                          <span>{t("foodRecommendations")}</span>
                        </h3>
                        <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                          {result.food_recommendations.map((food, idx) => (
                            <li key={idx}>{food}</li>
                          ))}
                        </ul>
                      </div>

                      {/* Hygiene suggestions */}
                      <div className="space-y-2">
                        <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                          <Stethoscope className="w-4 h-4 text-cyan-400" />
                          <span>{t("hygieneSuggestions")}</span>
                        </h3>
                        <ul className="list-disc list-inside text-slate-400 text-sm space-y-1">
                          {result.hygiene_tips.map((tip, idx) => (
                            <li key={idx}>{tip}</li>
                          ))}
                        </ul>
                      </div>
                    </div>

                    {/* Warnings / Doctor disclaimer */}
                    <div className="bg-amber-500/10 border border-amber-500/20 rounded-xl p-4 flex items-start space-x-3 mt-4">
                      <AlertTriangle className="w-5 h-5 text-amber-500 shrink-0 mt-0.5" />
                      <div>
                        <h4 className="text-amber-500 text-xs font-extrabold uppercase tracking-wider">
                          {t("warningTitle")}
                        </h4>
                        <p className="text-slate-300 text-xs leading-relaxed mt-1">
                          {t("warningText")}
                        </p>
                      </div>
                    </div>
                  </div>
                </>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Emergency Red popup */}
      {result && (
        <EmergencyAlert
          isOpen={emergencyOpen}
          onClose={() => setEmergencyOpen(false)}
          diseaseName={result.disease_name}
          severity={result.severity}
          firstAid={result.first_aid}
        />
      )}
    </div>
  );
};

export default Detect;

