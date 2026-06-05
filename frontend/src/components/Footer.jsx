import React from "react";
import { useLanguage } from "../context/LanguageContext";

const Footer = () => {
  const { t } = useLanguage();

  return (
    <footer className="bg-slate-950 border-t border-slate-900 text-slate-400 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-4">
        <div className="flex justify-center items-center space-x-2">
          <span className="text-xl font-bold bg-gradient-to-r from-emerald-400 to-teal-500 bg-clip-text text-transparent">
            🐄 PashuCare AI
          </span>
        </div>
        <p className="text-sm max-w-md mx-auto">
          {t("heroSubtitle")}
        </p>
        <p className="text-xs text-slate-555">
          &copy; {new Date().getFullYear()} PashuCare AI. All rights reserved. Developed for cow, goat, and sheep farmers.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
