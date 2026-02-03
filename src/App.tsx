import { motion } from 'framer-motion';
import {
    Building2, Users, Settings, BarChart3, FileText, Bell, Search, ChevronDown,
    TrendingUp, MoreHorizontal, Plus, Download, Filter, ArrowUpRight, ArrowDownRight,
    CheckCircle2, AlertCircle, Clock, LayoutDashboard, Briefcase, MessageSquare,
    Shield, Zap, Sparkles
} from 'lucide-react';

const SIDEBAR_ITEMS = [
    { icon: LayoutDashboard, label: 'Dashboard', active: true },
    { icon: Users, label: 'Customers', active: false },
    { icon: Briefcase, label: 'Projects', active: false },
    { icon: FileText, label: 'Documents', active: false },
    { icon: BarChart3, label: 'Analytics', active: false },
    { icon: MessageSquare, label: 'Messages', active: false },
    { icon: Shield, label: 'Security', active: false },
    { icon: Settings, label: 'Settings', active: false },
];

const METRICS = [
    {
        label: 'Total Revenue',
        value: '$847,293',
        change: '+12.5%',
        trend: 'up' as const,
        period: 'vs last month',
        icon: TrendingUp,
        color: 'emerald',
        gradient: 'from-emerald-400 to-emerald-600'
    },
    {
        label: 'Active Users',
        value: '24,593',
        change: '+8.2%',
        trend: 'up' as const,
        period: 'vs last month',
        icon: Users,
        color: 'blue',
        gradient: 'from-primary-400 to-primary-600'
    },
    {
        label: 'Conversion Rate',
        value: '3.24%',
        change: '-0.4%',
        trend: 'down' as const,
        period: 'vs last month',
        icon: BarChart3,
        color: 'orange',
        gradient: 'from-orange-400 to-orange-600'
    },
    {
        label: 'Avg. Response',
        value: '142ms',
        change: '-12ms',
        trend: 'up' as const,
        period: 'vs last month',
        icon: Zap,
        color: 'violet',
        gradient: 'from-violet-400 to-violet-600'
    },
];

const RECENT_ACTIVITY = [
    { user: 'Sarah Chen', action: 'completed project', target: 'Enterprise Dashboard', time: '2 hours ago', status: 'success', avatar: 'SC' },
    { user: 'Mike Johnson', action: 'submitted proposal', target: 'Q2 Marketing Plan', time: '4 hours ago', status: 'pending', avatar: 'MJ' },
    { user: 'Emily Davis', action: 'approved invoice', target: 'INV-2024-1847', time: '5 hours ago', status: 'success', avatar: 'ED' },
    { user: 'Alex Kumar', action: 'requested review', target: 'Mobile App Redesign', time: '6 hours ago', status: 'warning', avatar: 'AK' },
];

const TOP_CLIENTS = [
    { name: 'TechCorp Industries', revenue: '$124,500', projects: 12, status: 'active', color: 'bg-emerald-500' },
    { name: 'Global Finance Ltd', revenue: '$98,200', projects: 8, status: 'active', color: 'bg-primary-500' },
    { name: 'Healthcare Plus', revenue: '$87,300', projects: 6, status: 'active', color: 'bg-violet-500' },
    { name: 'Startup Velocity', revenue: '$65,800', projects: 4, status: 'review', color: 'bg-orange-500' },
];

const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
        opacity: 1,
        transition: { staggerChildren: 0.05, delayChildren: 0.1 }
    }
};

const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
        opacity: 1,
        y: 0,
        transition: { type: 'spring' as const, stiffness: 300, damping: 30 }
    }
};

function App() {
    return (
        <div className="min-h-screen bg-slate-50">
            {/* Sidebar */}
            <aside className="nexus-sidebar">
                <div className="nexus-sidebar-header">
                    <div className="flex items-center gap-4">
                        <div className="w-12 h-12 bg-gradient-to-br from-primary-500 via-primary-600 to-violet-600 rounded-xl flex items-center justify-center shadow-lg shadow-primary-500/30">
                            <Building2 className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <h1 className="text-xl font-bold text-slate-900">NEXUS</h1>
                            <p className="text-xs font-medium text-slate-500">Enterprise Suite</p>
                        </div>
                    </div>
                </div>

                <nav className="nexus-sidebar-nav nexus-scrollbar">
                    <div className="px-4 mb-3 text-xs font-bold text-slate-400 uppercase tracking-wider">
                        Main Menu
                    </div>
                    {SIDEBAR_ITEMS.map((item) => {
                        const Icon = item.icon;
                        return (
                            <div
                                key={item.label}
                                className={`nexus-nav-item ${item.active ? 'nexus-nav-item-active' : ''}`}
                            >
                                <Icon className="w-5 h-5" />
                                <span>{item.label}</span>
                                {item.active && (
                                    <motion.div
                                        layoutId="activeIndicator"
                                        className="ml-auto w-1.5 h-1.5 rounded-full bg-primary-500"
                                    />
                                )}
                            </div>
                        );
                    })}
                </nav>

                <div className="p-4 border-t border-slate-100">
                    <div className="flex items-center gap-3 p-3 bg-slate-50 rounded-xl border border-slate-100 hover:border-slate-200 transition-colors cursor-pointer">
                        <div className="nexus-avatar">
                            <span>JD</span>
                        </div>
                        <div className="flex-1 min-w-0">
                            <p className="text-sm font-semibold text-slate-900 truncate">John Doe</p>
                            <p className="text-xs font-medium text-slate-500">Administrator</p>
                        </div>
                        <ChevronDown className="w-4 h-4 text-slate-400" />
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <main className="nexus-main">
                {/* Top Bar */}
                <header className="nexus-topbar">
                    <div className="flex items-center gap-4 flex-1">
                        <div className="relative w-96">
                            <Search className="w-4 h-4 absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" />
                            <input
                                type="text"
                                placeholder="Search projects, clients, or reports..."
                                className="nexus-input pl-11 bg-slate-50/50"
                            />
                        </div>
                    </div>

                    <div className="flex items-center gap-3">
                        <button className="nexus-btn-icon relative">
                            <Bell className="w-5 h-5" />
                            <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full ring-2 ring-white"></span>
                        </button>
                        <button className="nexus-btn-primary gap-2">
                            <Plus className="w-4 h-4" />
                            <span>New Project</span>
                        </button>
                    </div>
                </header>

                <div className="p-8">
                    {/* Page Header */}
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="flex items-center justify-between mb-8"
                    >
                        <div>
                            <div className="flex items-center gap-3 mb-1">
                                <h1 className="nexus-section-title">Dashboard</h1>
                                <span className="nexus-badge-info">Pro Plan</span>
                            </div>
                            <p className="nexus-section-subtitle">
                                Welcome back! Here's what's happening with your business today.
                            </p>
                        </div>
                        <div className="flex items-center gap-3">
                            <button className="nexus-btn-secondary gap-2">
                                <Download className="w-4 h-4" />
                                <span>Export</span>
                            </button>
                            <button className="nexus-btn-secondary gap-2">
                                <Filter className="w-4 h-4" />
                                <span>Filter</span>
                            </button>
                        </div>
                    </motion.div>

                    {/* Metrics Grid */}
                    <motion.div
                        variants={containerVariants}
                        initial="hidden"
                        animate="visible"
                        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8"
                    >
                        {METRICS.map((metric) => {
                            const Icon = metric.icon;
                            return (
                                <motion.div
                                    key={metric.label}
                                    variants={itemVariants}
                                    className="nexus-stat-card group cursor-pointer"
                                >
                                    <div className="flex items-start justify-between mb-4">
                                        <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${metric.gradient} flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                                            <Icon className="w-6 h-6 text-white" />
                                        </div>
                                        <span className={`nexus-badge-${metric.trend === 'up' ? 'success' : 'error'}`}>
                                            {metric.trend === 'up' ? (
                                                <ArrowUpRight className="w-3 h-3" />
                                            ) : (
                                                <ArrowDownRight className="w-3 h-3" />
                                            )}
                                            {metric.change}
                                        </span>
                                    </div>
                                    <p className="nexus-metric-label mb-1">{metric.label}</p>
                                    <p className="nexus-metric-value">{metric.value}</p>
                                    <p className="text-xs text-slate-400 mt-2 font-medium">{metric.period}</p>
                                </motion.div>
                            );
                        })}
                    </motion.div>

                    {/* Content Grid */}
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {/* Recent Activity */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.3 }}
                            className="lg:col-span-2 nexus-card"
                        >
                            <div className="nexus-card-header">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-100 to-primary-50 flex items-center justify-center">
                                        <Sparkles className="w-5 h-5 text-primary-600" />
                                    </div>
                                    <div>
                                        <h2 className="text-lg font-bold text-slate-900">Recent Activity</h2>
                                        <p className="text-xs text-slate-500 font-medium">Latest updates from your team</p>
                                    </div>
                                </div>
                                <button className="text-sm font-semibold text-primary-600 hover:text-primary-700 transition-colors">
                                    View All
                                </button>
                            </div>
                            <div className="divide-y divide-slate-100">
                                {RECENT_ACTIVITY.map((activity, idx) => (
                                    <motion.div
                                        key={idx}
                                        initial={{ opacity: 0, x: -10 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        transition={{ delay: 0.4 + idx * 0.05 }}
                                        className="nexus-activity-item"
                                    >
                                        <div className={`nexus-activity-icon ${
                                            activity.status === 'success' ? 'bg-emerald-100' :
                                            activity.status === 'pending' ? 'bg-amber-100' : 'bg-rose-100'
                                        }`}>
                                            {activity.status === 'success' ? (
                                                <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                                            ) : activity.status === 'pending' ? (
                                                <Clock className="w-5 h-5 text-amber-600" />
                                            ) : (
                                                <AlertCircle className="w-5 h-5 text-rose-600" />
                                            )}
                                        </div>
                                        <div className="flex-1 min-w-0">
                                            <p className="text-sm text-slate-900">
                                                <span className="font-semibold">{activity.user}</span>
                                                <span className="text-slate-500"> {activity.action} </span>
                                                <span className="font-semibold text-primary-600">{activity.target}</span>
                                            </p>
                                            <p className="text-xs text-slate-400 font-medium mt-0.5">{activity.time}</p>
                                        </div>
                                        <button className="nexus-btn-icon w-8 h-8 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <MoreHorizontal className="w-4 h-4" />
                                        </button>
                                    </motion.div>
                                ))}
                            </div>
                        </motion.div>

                        {/* Top Clients */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.4 }}
                            className="nexus-card"
                        >
                            <div className="nexus-card-header">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-violet-100 to-violet-50 flex items-center justify-center">
                                        <Building2 className="w-5 h-5 text-violet-600" />
                                    </div>
                                    <div>
                                        <h2 className="text-lg font-bold text-slate-900">Top Clients</h2>
                                        <p className="text-xs text-slate-500 font-medium">By revenue this month</p>
                                    </div>
                                </div>
                            </div>
                            <div className="divide-y divide-slate-100">
                                {TOP_CLIENTS.map((client, idx) => (
                                    <motion.div
                                        key={idx}
                                        initial={{ opacity: 0, x: 10 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        transition={{ delay: 0.5 + idx * 0.05 }}
                                        className="px-6 py-4 hover:bg-slate-50/80 transition-colors cursor-pointer group"
                                    >
                                        <div className="flex items-center gap-3 mb-3">
                                            <div className={`w-10 h-10 rounded-xl ${client.color} flex items-center justify-center text-white font-bold text-sm shadow-md group-hover:scale-110 transition-transform`}>
                                                {client.name.charAt(0)}
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <h3 className="font-semibold text-slate-900 text-sm truncate">{client.name}</h3>
                                                <p className="text-xs text-slate-500">{client.projects} active projects</p>
                                            </div>
                                            <span className={`nexus-badge-${client.status === 'active' ? 'success' : 'warning'}`}>
                                                {client.status}
                                            </span>
                                        </div>
                                        <div className="flex items-center justify-between pl-13">
                                            <span className="text-xl font-bold text-slate-900">{client.revenue}</span>
                                            <ArrowUpRight className="w-4 h-4 text-emerald-500 opacity-0 group-hover:opacity-100 transition-opacity" />
                                        </div>
                                    </motion.div>
                                ))}
                            </div>
                            <div className="px-6 py-4 border-t border-slate-100">
                                <button className="w-full text-center text-sm font-semibold text-primary-600 hover:text-primary-700 transition-colors py-2 rounded-xl hover:bg-primary-50">
                                    View All Clients
                                </button>
                            </div>
                        </motion.div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default App;
