import { motion } from 'framer-motion';
import { Server, Database, Zap, Shield, ArrowRight, Code2, Terminal, GitBranch, Layers, Cpu, Clock, Check, Github, Twitter, Linkedin } from 'lucide-react';

const FEATURES = [
    { icon: <Server />, title: "Rapid Prototyping", desc: "Scaffold production APIs in minutes with built-in ORM and routing." },
    { icon: <Shield />, title: "Battle-Tested Security", desc: "CSRF, XSS, and SQL injection protection enabled by default." },
    { icon: <Database />, title: "Flexible ORM", desc: "Support for PostgreSQL, MySQL, SQLite, and more with migrations." },
    { icon: <Zap />, title: "Async Ready", desc: "Full ASGI support for high-concurrency real-time applications." },
];

const COMMANDS = [
    { cmd: "$ pip install django", label: "Install Framework" },
    { cmd: "$ django-admin startproject myapp", label: "Bootstrap Project" },
    { cmd: "$ python manage.py runserver", label: "Start Dev Server" },
];

function App() {
    return (
        <div className="min-h-screen bg-slate-950 text-white">
            {/* Navigation */}
            <nav className="fixed top-0 left-0 right-0 h-20 bg-slate-950/80 backdrop-blur-2xl border-b border-white/5 z-50 px-6">
                <div className="max-w-7xl mx-auto h-full flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="w-10 h-10 bg-gradient-to-br from-green-500 to-emerald-400 rounded-xl flex items-center justify-center text-white shadow-lg shadow-green-500/20">
                            <Terminal className="w-5 h-5" />
                        </div>
                        <div>
                            <h1 className="text-lg font-black tracking-tight uppercase leading-none">PY<span className="text-green-400">STACK</span></h1>
                            <p className="text-[8px] font-bold text-slate-500 uppercase tracking-[0.2em]">Backend Framework Hub</p>
                        </div>
                    </div>

                    <div className="hidden md:flex items-center gap-10">
                        {['Quickstart', 'Docs', 'Ecosystem', 'Deploy'].map(l => (
                            <a key={l} href="#" className="text-xs font-bold uppercase tracking-widest text-slate-400 hover:text-green-400 transition-colors">{l}</a>
                        ))}
                    </div>

                    <button className="hidden sm:flex items-center gap-2 px-6 py-3 bg-green-500 hover:bg-green-600 text-white font-black rounded-xl transition-all text-xs uppercase tracking-widest shadow-lg shadow-green-500/20">
                        <GitBranch className="w-4 h-4" /> Clone Starter
                    </button>
                </div>
            </nav>

            <main className="pt-32 pb-20">
                {/* Hero Section */}
                <section className="max-w-7xl mx-auto px-6 mb-40 text-center">
                    <motion.div
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                    >
                        <span className="inline-flex items-center gap-2 px-5 py-2 bg-green-500/10 border border-green-500/20 rounded-full text-[10px] font-black uppercase tracking-widest text-green-400 mb-10">
                            <Cpu className="w-3 h-3" /> Python 3.12 Compatible
                        </span>

                        <h1 className="text-6xl md:text-[6rem] font-black leading-[0.85] tracking-tighter uppercase mb-10">
                            THE BACKEND <br /> <span className="text-transparent bg-clip-text bg-gradient-to-r from-green-400 to-emerald-400 italic">FRAMEWORK</span> <br /> FOR PERFECTIONISTS.
                        </h1>

                        <p className="text-xl text-slate-400 font-medium max-w-2xl mx-auto mb-16 leading-relaxed">
                            Build robust, scalable web applications with the world's most popular Python framework. From MVP to enterprise.
                        </p>

                        <div className="flex flex-col sm:flex-row gap-6 justify-center">
                            <button className="px-12 py-5 bg-white text-slate-900 font-black rounded-2xl hover:bg-green-500 hover:text-white transition-all text-xs uppercase tracking-widest shadow-2xl flex items-center justify-center gap-3 group">
                                Get Started <ArrowRight className="w-4 h-4 group-hover:translate-x-2 transition-transform" />
                            </button>
                            <button className="px-12 py-5 border-2 border-slate-800 hover:border-green-500 text-white font-black rounded-2xl transition-all text-xs uppercase tracking-widest flex items-center justify-center gap-3">
                                <Code2 className="w-4 h-4" /> View Docs
                            </button>
                        </div>
                    </motion.div>
                </section>

                {/* Terminal Preview */}
                <section className="max-w-4xl mx-auto px-6 mb-40">
                    <div className="bg-slate-900/50 backdrop-blur-xl border border-white/5 rounded-3xl overflow-hidden">
                        <div className="p-4 border-b border-white/5 flex items-center gap-3">
                            <div className="flex gap-2">
                                <div className="w-3 h-3 bg-red-500 rounded-full" />
                                <div className="w-3 h-3 bg-yellow-500 rounded-full" />
                                <div className="w-3 h-3 bg-green-500 rounded-full" />
                            </div>
                            <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Terminal</span>
                        </div>
                        <div className="p-8 space-y-6 font-mono text-sm">
                            {COMMANDS.map((c, i) => (
                                <motion.div
                                    key={i}
                                    initial={{ opacity: 0, x: -20 }}
                                    whileInView={{ opacity: 1, x: 0 }}
                                    viewport={{ once: true }}
                                    transition={{ delay: i * 0.2 }}
                                    className="flex items-center gap-4"
                                >
                                    <span className="text-green-400">{c.cmd}</span>
                                    <span className="text-[10px] font-bold text-slate-600 uppercase tracking-widest">// {c.label}</span>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* Features Grid */}
                <section className="max-w-7xl mx-auto px-6 mb-40">
                    <div className="text-center mb-20">
                        <h2 className="text-4xl md:text-6xl font-black tracking-tighter uppercase mb-4">CORE <span className="text-slate-700 italic">CAPABILITIES</span></h2>
                        <p className="text-sm font-bold text-slate-500 uppercase tracking-[0.3em]">Everything for backend excellence</p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                        {FEATURES.map((f, idx) => (
                            <motion.div
                                key={f.title}
                                initial={{ opacity: 0, y: 20 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                transition={{ delay: idx * 0.1 }}
                                className="p-10 bg-slate-900/50 backdrop-blur-xl border border-white/5 rounded-3xl group hover:border-green-500/50 transition-all"
                            >
                                <div className="w-16 h-16 bg-green-500/10 border border-green-500/20 rounded-2xl flex items-center justify-center text-green-400 mb-8 group-hover:bg-green-500 group-hover:text-white transition-all">
                                    {f.icon}
                                </div>
                                <h3 className="text-2xl font-black uppercase tracking-tight mb-4">{f.title}</h3>
                                <p className="text-slate-400 font-medium leading-relaxed">{f.desc}</p>
                            </motion.div>
                        ))}
                    </div>
                </section>

                {/* CTA Section */}
                <section className="py-32 bg-gradient-to-b from-slate-900 to-slate-950 border-y border-white/5 text-center">
                    <div className="max-w-4xl mx-auto px-6">
                        <Layers className="w-16 h-16 text-green-400 mx-auto mb-10" />
                        <h2 className="text-5xl md:text-6xl font-black uppercase tracking-tighter mb-10 leading-none">
                            START <span className="text-transparent bg-clip-text bg-gradient-to-r from-green-400 to-emerald-400 italic">BUILDING</span> TODAY.
                        </h2>
                        <p className="text-lg text-slate-400 font-medium mb-12 max-w-xl mx-auto">
                            Clone the starter template, customize, and deploy to production in minutes.
                        </p>

                        <button className="px-16 py-6 bg-gradient-to-r from-green-500 to-emerald-500 text-white font-black rounded-2xl hover:scale-105 transition-transform text-sm uppercase tracking-widest shadow-2xl shadow-green-500/30">
                            Get the Starter Kit
                        </button>
                    </div>
                </section>
            </main>

            {/* Footer */}
            <footer className="border-t border-white/5 py-16 px-6">
                <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-10">
                    <div className="flex items-center gap-2">
                        <Terminal className="w-5 h-5 text-green-400" />
                        <span className="font-black uppercase tracking-tight">PY<span className="text-green-400">STACK</span></span>
                    </div>
                    <div className="flex gap-6">
                        {[Github, Twitter, Linkedin].map((Icon, i) => (
                            <button key={i} className="p-3 bg-white/5 border border-white/10 hover:bg-green-500 hover:text-white transition-all rounded-xl">
                                <Icon className="w-5 h-5" />
                            </button>
                        ))}
                    </div>
                    <p className="text-[10px] font-black text-slate-600 uppercase tracking-[0.4em]">© 2026 PYSTACK // BACKEND • 22/30 DISPATCHED</p>
                </div>
            </footer>
        </div>
    );
}

export default App;
