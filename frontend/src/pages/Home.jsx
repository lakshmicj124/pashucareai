import React from "react";
import { Link } from "react-router-dom";
import { useLanguage } from "../context/LanguageContext";
import { useAuth } from "../context/AuthContext";
import { Shield, Sparkles, MapPin, Globe, History, Activity, AlertTriangle, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

const Home = () => {
  const { t } = useLanguage();
  const { user } = useAuth();

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.15 }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: { y: 0, opacity: 1 }
  };

  return (
    <div className="bg-slate-950 text-white min-h-screen">
      {/* Hero Section */}
      <section className="relative overflow-hidden py-20 px-4 sm:px-6 lg:px-8 border-b border-slate-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-emerald-950/20 via-slate-950 to-slate-950">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#0f172a_1px,transparent_1px),linear-gradient(to_bottom,#0f172a_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] opacity-40"></div>
        <div className="max-w-7xl mx-auto text-center relative z-10 space-y-8">
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center space-x-2 bg-emerald-500/10 border border-emerald-500/30 px-4 py-1.5 rounded-full text-emerald-400 text-sm font-semibold"
          >
            <Sparkles className="w-4 h-4" />
            <span>AI Livestock Diagnostic System</span>
          </motion.div>
          
          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-4xl sm:text-6xl font-extrabold tracking-tight bg-linear-to-r from-emerald-400 via-teal-350 to-cyan-400 bg-clip-text text-transparent max-w-4xl mx-auto leading-tight"
          >
            {t("heroTitle")}
          </motion.h1>

          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed"
          >
            {t("heroSubtitle")}
          </motion.p>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3 }}
            className="flex flex-col sm:flex-row justify-center gap-4"
          >
            <Link
              to="/detect"
              className="flex items-center justify-center space-x-2 bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-extrabold px-8 py-4 rounded-xl shadow-lg shadow-emerald-500/25 transition-all text-lg cursor-pointer"
            >
              <span>{t("startDetection")}</span>
              <ArrowRight className="w-5 h-5" />
            </Link>
            {user && (
              <Link
                to="/history"
                className="flex items-center justify-center space-x-2 bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-200 font-semibold px-8 py-4 rounded-xl transition-all text-lg"
              >
                <History className="w-5 h-5 text-emerald-450" />
                <span>{t("viewHistory")}</span>
              </Link>
            )}
          </motion.div>
        </div>
      </section>

      {/* Stats/Supported Animals Section */}
      <section className="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            {
              emoji: "🐄",
              name: t("cow"),
              symptoms: "Lumpy Skin, Mastitis, Foot & Mouth, Bloat, Black Quarter",
              color: "border-emerald-500/30 bg-emerald-950/10 text-emerald-400"
            },
            {
              emoji: "🐐",
              name: t("goat"),
              symptoms: "PPR, Goat Pox, Contagious Ecthyma (Orf), Enterotoxemia",
              color: "border-teal-500/30 bg-teal-950/10 text-teal-400"
            },
            {
              emoji: "🐑",
              name: t("sheep"),
              symptoms: "Foot Rot, Sheep Scab, Blue Tongue, Pneumonia",
              color: "border-cyan-500/30 bg-cyan-950/10 text-cyan-400"
            }
          ].map((animal, idx) => (
            <motion.div
              key={idx}
              whileHover={{ y: -5 }}
              className={`border p-6 rounded-2xl ${animal.color} transition-all`}
            >
              <div className="text-5xl mb-4">{animal.emoji}</div>
              <h3 className="text-2xl font-bold mb-2">{animal.name}</h3>
              <p className="text-slate-450 text-sm leading-relaxed">
                <span className="font-semibold block mb-1 text-slate-300">Supported Diagnostics:</span>
                {animal.symptoms}
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Core Features Grid */}
      <section className="py-20 bg-slate-900/40 border-t border-slate-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
          <div className="text-center space-y-4">
            <h2 className="text-3xl sm:text-4xl font-extrabold">{t("keyFeatures")}</h2>
            <p className="text-slate-400 max-w-xl mx-auto">
              A comprehensive system designed for easy utility on the farm.
            </p>
          </div>

          <motion.div
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            {/* Feature 1 */}
            <motion.div variants={itemVariants} className="bg-slate-900 border border-slate-800 p-8 rounded-2xl space-y-4">
              <div className="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
                <Activity className="w-6 h-6 text-emerald-400" />
              </div>
              <h3 className="text-xl font-bold">{t("featureAiTitle")}</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                {t("featureAiDesc")}
              </p>
            </motion.div>

            {/* Feature 2 */}
            <motion.div variants={itemVariants} className="bg-slate-900 border border-slate-800 p-8 rounded-2xl space-y-4">
              <div className="w-12 h-12 rounded-xl bg-teal-500/10 border border-teal-500/30 flex items-center justify-center">
                <MapPin className="w-6 h-6 text-teal-400" />
              </div>
              <h3 className="text-xl font-bold">{t("featureVetTitle")}</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                {t("featureVetDesc")}
              </p>
            </motion.div>

            {/* Feature 3 */}
            <motion.div variants={itemVariants} className="bg-slate-900 border border-slate-800 p-8 rounded-2xl space-y-4">
              <div className="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center">
                <Globe className="w-6 h-6 text-cyan-400" />
              </div>
              <h3 className="text-xl font-bold">{t("featureLangTitle")}</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                {t("featureLangDesc")}
              </p>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Disclaimer / Veterinary Warning banner */}
      <section className="py-12 bg-amber-500/10 border-y border-amber-500/20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-12 rounded-2xl flex items-start gap-4">
        <AlertTriangle className="w-8 h-8 text-amber-500 shrink-0 mt-1" />
        <div className="space-y-1">
          <h4 className="text-amber-500 font-extrabold uppercase text-sm tracking-wider">
            {t("warningTitle")}
          </h4>
          <p className="text-slate-300 text-sm leading-relaxed">
            {t("warningText")}
          </p>
        </div>
      </section>
    </div>
  );
};

export default Home;

