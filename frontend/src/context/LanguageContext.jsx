import React, { createContext, useState, useContext, useEffect } from "react";
import translations from "../i18n/translations.json";

const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  // Load saved language or default to 'en'
  const [language, setLanguage] = useState(() => {
    return localStorage.getItem("pashucare_lang") || "en";
  });

  useEffect(() => {
    localStorage.setItem("pashucare_lang", language);
  }, [language]);

  const t = (key) => {
    const langObj = translations[language] || translations["en"];
    return langObj[key] || translations["en"][key] || key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
