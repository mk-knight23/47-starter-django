import { motion } from 'framer-motion';
import { Building2, Users, Settings, BarChart3, FileText, Bell, Search, ChevronDown, TrendingUp, TrendingDown, MoreHorizontal, Plus, Download, Filter, Calendar, ArrowUpRight, ArrowDownRight, CheckCircle2, AlertCircle, Clock } from 'lucide-react';

const SIDEBAR_ITEMS = [
    { icon: <BarChart3 className="w-5 h-5" />, label: 'Dashboard', active: true },
    { icon: <Users className="w-5 h-5" />, label: 'Customers', active: false },
    { icon: <FileText className="w-5 h-5" />, label: 'Projects', active: false },
    { icon: <Settings className="w-5 h-5" />, label: 'Settings', active: false },
];

const METRICS = [
    { label: 'Total Revenue', value: '$847,293', change: '+12.5%', trend: 'up', period: 'vs last month' },
    { label: 'Active Users', value: '24,593', change: '+8.2%', trend: 'up', period: 'vs last month' },
    { label: 'Conversion Rate', value: '3.24%', change: '-0.4%', trend: 'down', period: 'vs last month' },
    { label: 'Avg. Response Time', value: '142ms', change: '-12ms', trend: 'up', period: 'vs last month' },
];

const RECENT_ACTIVITY = [
    { user: 'Sarah Chen', action: 'completed project', target: 'Enterprise Dashboard', time: '2 hours ago', status: 'success' },
    { user: 'Mike Johnson', action: 'submitted proposal', target: 'Q2 Marketing Plan', time: '4 hours ago', status: 'pending' },
    { user: 'Emily Davis', action: 'approved invoice', target: 'INV-2024-1847', time: '5 hours ago', status: 'success' },
    { user: 'Alex Kumar', action: 'requested review', target: 'Mobile App Redesign', time: '6 hours ago', status: 'warning' },
];

const TOP_CLIENTS = [
    { name: 'TechCorp Industries', revenue: '$124,500', projects: 12, status: 'active' },
    { name: 'Global Finance Ltd', revenue: '$98,200', projects: 8, status: 'active' },
    { name: 'Healthcare Plus', revenue: '$87,300', projects: 6, status: 'active' },
    { name: 'Startup Velocity', revenue: '$65,800', projects: 4, status: 'review' },
];

function App() {
    return (
        <div className="min-h-screen bg-slate-50">
            {/* Sidebar */}
            <aside className="enterprise-sidebar">
                <div className="p-6 border-b border-slate-200">
                    <div className="flex items-center gap-3">
                        <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
                            <Building2 className="w-6 h-6 text-white" />
                        </div>
                        <div>
                            <h1 className="text-lg font-bold text-slate-900">NEXUS</h1>
                            <p className="text-xs text-slate-500">Enterprise Suite</p>
                        </div>
                    </div>
                </div>

                <nav className="flex-1 py-6">
                    <div className="px-4 mb-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">Main Menu</div>
                    {SIDEBAR_ITEMS.map((item) => (
                        <div key={item.label} className={`enterprise-nav-item ${item.active ? 'enterprise-nav-item-active' : ''}`}>
                            {item.icon}
                            <span>{item.label}</span>
                        </div>
                    ))}
                </nav>

                <div className="p-4 border-t border-slate-200">
                    <div className="flex items-center gap-3 p-3 bg-slate-50 rounded-lg">
                        <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                            <span className="text-sm font-semibold text-blue-600">JD</span>
                        </div>
                        <div className="flex-1">
                            <p className="text-sm font-medium text-slate-900">John Doe</p>
                            <p className="text-xs text-slate-500">Admin</p>
                        </div>
                        <ChevronDown className="w-4 h-4 text-slate-400" />
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <main className="ml-64">
                {/* Top Bar */}
                <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 sticky top-0 z-30">
                    <div className="flex items-center gap-4 flex-1">
                        <div className="relative w-80">
                            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                            <input
                                type="text"
                                placeholder="Search projects, clients, or reports..."
                                className="enterprise-input pl-10"
                            />
                        </div>
                    </div>

                    <div className="flex items-center gap-4">
                        <button className="relative p-2 text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-lg transition-colors">
                            <Bell className="w-5 h-5" />
                            <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
                        </button>
                        <button className="enterprise-button-primary gap-2">
                            <Plus className="w-4 h-4" /> New Project
                        </button>
                    </div>
                </header>

                <div className="p-8">
                    {/* Page Header */}
                    <div className="flex items-center justify-between mb-8">
                        <div>
                            <h1 className="text-2xl font-bold text-slate-900">Dashboard</h1>
                            <p className="text-slate-500 mt-1">Welcome back, John. Here's what's happening today.</p>
                        </div>
                        <div className="flex items-center gap-3">
                            <button className="enterprise-button-secondary gap-2">
                                <Download className="w-4 h-4" /> Export
                            </button>
                            <button className="enterprise-button-primary gap-2">
                                <Filter className="w-4 h-4" /> Filter
                            </button>
                        </div>
                    </div>

                    {/* Metrics Grid */}
                    <div className="grid grid-cols-4 gap-6 mb-8">
                        {METRICS.map((metric, idx) => (
                            <motion.div
                                key={metric.label}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.1 }}
                                className="enterprise-stat-card"
                            >
                                <div className="flex items-center justify-between mb-4">
                                    <p className="text-sm font-medium text-slate-500">{metric.label}</p>
                                    <span className={`enterprise-badge ${metric.trend === 'up' ? 'enterprise-badge-success' : metric.trend === 'down' ? 'enterprise-badge-danger' : 'enterprise-badge-info'}`}>
                                        {metric.change}
                                    </span>
                                </div>
                                <p className="text-3xl font-bold text-slate-900 mb-1">{metric.value}</p>
                                <div className="flex items-center gap-1 text-xs text-slate-500">
                                    {metric.trend === 'up' ? <ArrowUpRight className="w-3 h-3 text-emerald-500" /> : <ArrowDownRight className="w-3 h-3 text-red-500" />}
                                    <span>{metric.period}</span>
                                </div>
                            </motion.div>
                        ))}
                    </div>

                    <div className="grid grid-cols-3 gap-6">
                        {/* Recent Activity */}
                        <div className="col-span-2 enterprise-card">
                            <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between">
                                <h2 className="text-lg font-semibold text-slate-900">Recent Activity</h2>
                                <button className="text-sm text-blue-600 hover:text-blue-700 font-medium">View All</button>
                            </div>
                            <div className="divide-y divide-slate-100">
                                {RECENT_ACTIVITY.map((activity, idx) => (
                                    <div key={idx} className="px-6 py-4 flex items-center gap-4 hover:bg-slate-50 transition-colors">
                                        <div className={`w-10 h-10 rounded-full flex items-center justify-center ${
                                            activity.status === 'success' ? 'bg-emerald-100' :
                                            activity.status === 'pending' ? 'bg-amber-100' : 'bg-red-100'
                                        }`}>
                                            {activity.status === 'success' ? (
                                                <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                                            ) : activity.status === 'pending' ? (
                                                <Clock className="w-5 h-5 text-amber-600" />
                                            ) : (
                                                <AlertCircle className="w-5 h-5 text-red-600" />
                                            )}
                                        </div>
                                        <div className="flex-1">
                                            <p className="text-sm text-slate-900">
                                                <span className="font-semibold">{activity.user}</span>
                                                <span className="text-slate-500"> {activity.action} </span>
                                                <span className="font-medium text-blue-600">{activity.target}</span>
                                            </p>
                                            <p className="text-xs text-slate-400 mt-0.5">{activity.time}</p>
                                        </div>
                                        <button className="p-2 hover:bg-slate-100 rounded-lg transition-colors">
                                            <MoreHorizontal className="w-4 h-4 text-slate-400" />
                                        </button>
                                    </div>
                                ))}
                            </div>
                        </div>

                        {/* Top Clients */}
                        <div className="enterprise-card">
                            <div className="px-6 py-4 border-b border-slate-200">
                                <h2 className="text-lg font-semibold text-slate-900">Top Clients</h2>
                            </div>
                            <div className="divide-y divide-slate-100">
                                {TOP_CLIENTS.map((client, idx) => (
                                    <div key={idx} className="px-6 py-4 hover:bg-slate-50 transition-colors">
                                        <div className="flex items-center justify-between mb-2">
                                            <h3 className="font-medium text-slate-900 text-sm">{client.name}</h3>
                                            <span className={`enterprise-badge ${client.status === 'active' ? 'enterprise-badge-success' : 'enterprise-badge-warning'}`}>
                                                {client.status}
                                            </span>
                                        </div>
                                        <div className="flex items-center justify-between">
                                            <span className="text-lg font-bold text-slate-900">{client.revenue}</span>
                                            <span className="text-xs text-slate-500">{client.projects} projects</span>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className="px-6 py-4 border-t border-slate-200">
                                <button className="w-full text-center text-sm text-blue-600 hover:text-blue-700 font-medium">
                                    View All Clients
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default App;
