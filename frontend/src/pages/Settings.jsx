import React, { useState } from "react";
import { useLanguage } from "../context/LanguageContext";
import { useAuth } from "../context/AuthContext";
import { useTheme } from "../context/ThemeContext";
import api from "../services/api";
import { 
  Settings as SettingsIcon, Globe, Moon, User, Lock, 
  ShieldAlert, BadgeInfo, CheckCircle, AlertTriangle 
} from "lucide-react";
import { motion } from "framer-motion";

const Settings = () => {
  const { t, language, setLanguage } = useLanguage();
  const { user, setUser } = useAuth();
  const { darkMode, setDarkMode } = useTheme();

  // Profile Form State
  const [name, setName] = useState(user?.name || "");
  const [email, setEmail] = useState(user?.email || "");
  const [phone, setPhone] = useState(user?.phone_number || "");
  const [profileLoading, setProfileLoading] = useState(false);
  const [profileError, setProfileError] = useState("");
  const [profileSuccess, setProfileSuccess] = useState("");

  // Password Form State
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmNewPassword, setConfirmNewPassword] = useState("");
  const [passwordLoading, setPasswordLoading] = useState(false);
  const [passwordError, setPasswordError] = useState("");
  const [passwordSuccess, setPasswordSuccess] = useState("");

  const handleLanguageChange = (e) => {
    setLanguage(e.target.value);
  };

  const handleProfileUpdate = async (e) => {
    e.preventDefault();
    setProfileError("");
    setProfileSuccess("");

    if (!name || !email || !phone) {
      setProfileError("All fields are required.");
      return;
    }

    // Phone format check
    const phoneRegex = /^(\+91[\-\s]?)?[0-9]{10}$/;
    if (!phoneRegex.test(phone)) {
      setProfileError("Please enter a valid 10-digit phone number.");
      return;
    }

    setProfileLoading(true);
    try {
      const response = await api.put("/api/auth/profile", {
        name,
        email,
        phone_number: phone
      });
      setUser(response.data);
      setProfileSuccess("Profile updated successfully!");
    } catch (err) {
      console.error(err);
      setProfileError(err.response?.data?.detail || "Failed to update profile.");
    } finally {
      setProfileLoading(false);
    }
  };

  const handlePasswordUpdate = async (e) => {
    e.preventDefault();
    setPasswordError("");
    setPasswordSuccess("");

    if (!currentPassword || !newPassword || !confirmNewPassword) {
      setPasswordError("All password fields are required.");
      return;
    }

    if (newPassword.length < 8) {
      setPasswordError("New password must be at least 8 characters long.");
      return;
    }

    const specialCharRegex = /[!@#$%^&*(),.?":{}|<>_]/;
    if (!specialCharRegex.test(newPassword)) {
      setPasswordError("New password must include at least one special character.");
      return;
    }

    if (newPassword !== confirmNewPassword) {
      setPasswordError("New passwords do not match.");
      return;
    }

    setPasswordLoading(true);
    try {
      await api.put("/api/auth/password", {
        current_password: currentPassword,
        new_password: newPassword
      });
      setPasswordSuccess("Password changed successfully!");
      setCurrentPassword("");
      setNewPassword("");
      setConfirmNewPassword("");
    } catch (err) {
      console.error(err);
      setPasswordError(err.response?.data?.detail || "Failed to update password.");
    } finally {
      setPasswordLoading(false);
    }
  };

  return (
    <div className="bg-slate-950 text-white min-h-screen py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto space-y-8">
        
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-transparent bg-clip-text bg-linear-to-r from-emerald-400 to-teal-400">
            {t("settingsTitle")}
          </h1>
          <p className="text-slate-400 text-sm">
            {t("settingsDesc")}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          {/* Profile Form */}
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
            <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2 border-b border-slate-800 pb-3">
              <User className="w-4 h-4 text-emerald-450" />
              <span>Update Profile</span>
            </h3>

            {profileError && (
              <div className="bg-red-500/10 border border-red-500/20 rounded-xl p-3 flex items-center space-x-2 text-red-400 text-xs">
                <AlertTriangle className="w-4 h-4 shrink-0" />
                <span>{profileError}</span>
              </div>
            )}

            {profileSuccess && (
              <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-xl p-3 flex items-center space-x-2 text-emerald-450 text-xs">
                <CheckCircle className="w-4 h-4 shrink-0" />
                <span>{profileSuccess}</span>
              </div>
            )}

            <form onSubmit={handleProfileUpdate} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">Full Name</label>
                <input 
                  type="text" 
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">Email Address</label>
                <input 
                  type="email" 
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">Phone Number</label>
                <input 
                  type="tel" 
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  placeholder="+91 9876543210"
                  required
                />
              </div>

              <button 
                type="submit"
                disabled={profileLoading}
                className="w-full py-2.5 bg-emerald-500 hover:bg-emerald-600 disabled:bg-slate-700 text-slate-950 font-extrabold rounded-xl transition cursor-pointer text-sm shadow-md"
              >
                {profileLoading ? "Updating..." : "Save Profile Details"}
              </button>
            </form>
          </div>

          {/* Password Change Form */}
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
            <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2 border-b border-slate-800 pb-3">
              <Lock className="w-4 h-4 text-cyan-400" />
              <span>Change Password</span>
            </h3>

            {passwordError && (
              <div className="bg-red-500/10 border border-red-500/20 rounded-xl p-3 flex items-center space-x-2 text-red-400 text-xs">
                <AlertTriangle className="w-4 h-4 shrink-0" />
                <span>{passwordError}</span>
              </div>
            )}

            {passwordSuccess && (
              <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-xl p-3 flex items-center space-x-2 text-emerald-450 text-xs">
                <CheckCircle className="w-4 h-4 shrink-0" />
                <span>{passwordSuccess}</span>
              </div>
            )}

            <form onSubmit={handlePasswordUpdate} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">Current Password</label>
                <input 
                  type="password" 
                  value={currentPassword}
                  onChange={(e) => setCurrentPassword(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">New Password</label>
                <input 
                  type="password" 
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  placeholder="At least 8 chars + special char"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-450 mb-1">Confirm New Password</label>
                <input 
                  type="password" 
                  value={confirmNewPassword}
                  onChange={(e) => setConfirmNewPassword(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  required
                />
              </div>

              <button 
                type="submit"
                disabled={passwordLoading}
                className="w-full py-2.5 bg-cyan-500 hover:bg-cyan-600 disabled:bg-slate-700 text-slate-950 font-extrabold rounded-xl transition cursor-pointer text-sm shadow-md"
              >
                {passwordLoading ? "Updating..." : "Update Password"}
              </button>
            </form>
          </div>

        </div>

        {/* Preferences & Theme settings panel */}
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-6">
          <h3 className="text-sm font-extrabold text-slate-300 uppercase tracking-wider flex items-center space-x-2 border-b border-slate-800 pb-3">
            <SettingsIcon className="w-4 h-4 text-emerald-400" />
            <span>Preferences</span>
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Language Selector */}
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-slate-950/40 p-4 rounded-2xl border border-slate-850">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-slate-200 flex items-center space-x-2">
                  <Globe className="w-4 h-4 text-emerald-400" />
                  <span>{t("languageSelect")}</span>
                </h4>
                <p className="text-xs text-slate-400">{t("languageSelectDesc")}</p>
              </div>
              <select
                value={language}
                onChange={handleLanguageChange}
                className="bg-slate-900 border border-slate-850 text-white px-4 py-2 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
              >
                <option value="en">{t("english")}</option>
                <option value="kn">{t("kannada")}</option>
                <option value="hi">{t("hindi")}</option>
              </select>
            </div>

            {/* Theme Selector */}
            <div className="flex justify-between items-center bg-slate-950/40 p-4 rounded-2xl border border-slate-850">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-slate-200 flex items-center space-x-2">
                  <Moon className="w-4 h-4 text-cyan-400" />
                  <span>{t("darkMode")}</span>
                </h4>
                <p className="text-xs text-slate-400">{t("darkModeDesc")}</p>
              </div>
              <button
                type="button"
                onClick={() => setDarkMode(!darkMode)}
                className={`w-14 h-8 flex items-center rounded-full p-1 cursor-pointer transition-colors duration-300 ${
                  darkMode ? "bg-emerald-500" : "bg-slate-700"
                }`}
              >
                <div
                  className={`bg-slate-950 w-6 h-6 rounded-full shadow-md transform transition-transform duration-300 ${
                    darkMode ? "translate-x-6" : ""
                  }`}
                />
              </button>
            </div>
          </div>
        </div>

        {/* Info Card footer */}
        <div className="bg-slate-900/50 p-4 rounded-2xl border border-slate-850 flex items-start space-x-3 text-slate-400">
          <BadgeInfo className="w-5 h-5 text-emerald-450 shrink-0 mt-0.5" />
          <div className="space-y-1 text-xs">
            <p className="font-semibold text-slate-350">{t("systemDiagnostics")}</p>
            <p>{t("deviceConnectivity")}</p>
            <p>{t("aiEngineVersion")} {t("appVersion")}</p>
          </div>
        </div>

      </div>
    </div>
  );
};

export default Settings;

