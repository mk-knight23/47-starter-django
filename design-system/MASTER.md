# NEXUS Design System v2.0

## Design Philosophy
Bright, modern, confident SaaS aesthetic with high contrast and vibrant accent colors.

## Color Palette

### Primary Colors
- **Primary 50**: #eff6ff
- **Primary 100**: #dbeafe
- **Primary 200**: #bfdbfe
- **Primary 300**: #93c5fd
- **Primary 400**: #60a5fa
- **Primary 500**: #3b82f6
- **Primary 600**: #2563eb
- **Primary 700**: #1d4ed8
- **Primary 800**: #1e40af
- **Primary 900**: #1e3a8a

### Accent Colors (Vibrant)
- **Cyan**: #06b6d4
- **Teal**: #14b8a6
- **Emerald**: #10b981
- **Violet**: #8b5cf6
- **Fuchsia**: #d946ef
- **Orange**: #f97316
- **Rose**: #f43f5e
- **Amber**: #f59e0b

### Neutral Colors
- **White**: #ffffff
- **Slate 50**: #f8fafc
- **Slate 100**: #f1f5f9
- **Slate 200**: #e2e8f0
- **Slate 300**: #cbd5e1
- **Slate 400**: #94a3b8
- **Slate 500**: #64748b
- **Slate 600**: #475569
- **Slate 700**: #334155
- **Slate 800**: #1e293b
- **Slate 900**: #0f172a

## Typography

### Font Family
- **Primary**: 'Inter', system-ui, -apple-system, sans-serif
- **Monospace**: 'JetBrains Mono', 'Fira Code', monospace

### Font Sizes
- **xs**: 0.75rem (12px)
- **sm**: 0.875rem (14px)
- **base**: 1rem (16px)
- **lg**: 1.125rem (18px)
- **xl**: 1.25rem (20px)
- **2xl**: 1.5rem (24px)
- **3xl**: 1.875rem (30px)
- **4xl**: 2.25rem (36px)

### Font Weights
- **Normal**: 400
- **Medium**: 500
- **Semibold**: 600
- **Bold**: 700

## Spacing System
- **0**: 0
- **1**: 0.25rem (4px)
- **2**: 0.5rem (8px)
- **3**: 0.75rem (12px)
- **4**: 1rem (16px)
- **5**: 1.25rem (20px)
- **6**: 1.5rem (24px)
- **8**: 2rem (32px)
- **10**: 2.5rem (40px)
- **12**: 3rem (48px)
- **16**: 4rem (64px)

## Border Radius
- **sm**: 0.375rem (6px)
- **DEFAULT**: 0.5rem (8px)
- **md**: 0.625rem (10px)
- **lg**: 0.75rem (12px)
- **xl**: 1rem (16px)
- **2xl**: 1.5rem (24px)
- **full**: 9999px

## Shadows
- **sm**: 0 1px 2px 0 rgb(0 0 0 / 0.05)
- **DEFAULT**: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)
- **md**: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)
- **lg**: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)
- **xl**: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)
- **2xl**: 0 25px 50px -12px rgb(0 0 0 / 0.25)
- **inner**: inset 0 2px 4px 0 rgb(0 0 0 / 0.05)

## Component Styles

### Buttons
- **Primary**: bg-primary-600, text-white, hover:bg-primary-700, rounded-xl
- **Secondary**: bg-white, border-2 border-slate-200, text-slate-700, hover:border-primary-300, hover:bg-primary-50
- **Ghost**: transparent, text-slate-600, hover:bg-slate-100

### Cards
- **Default**: bg-white, rounded-2xl, shadow-sm, border border-slate-100
- **Hover**: hover:shadow-lg, hover:shadow-primary-100/50, transition-all duration-300
- **Gradient Border**: border-gradient from-primary-500 to-violet-500

### Inputs
- **Default**: bg-white, border-2 border-slate-200, rounded-xl, focus:border-primary-500, focus:ring-4 focus:ring-primary-100

### Badges
- **Success**: bg-emerald-100, text-emerald-700, border border-emerald-200
- **Warning**: bg-amber-100, text-amber-700, border border-amber-200
- **Error**: bg-rose-100, text-rose-700, border border-rose-200
- **Info**: bg-primary-100, text-primary-700, border border-primary-200
- **Neutral**: bg-slate-100, text-slate-700, border border-slate-200

## Animation
- **Fast**: 150ms
- **Normal**: 250ms
- **Slow**: 350ms
- **Easing**: cubic-bezier(0.4, 0, 0.2, 1)
- **Spring**: cubic-bezier(0.34, 1.56, 0.64, 1)

## Layout Patterns
- **Bento Grid**: grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6
- **Dashboard**: sidebar (280px) + main content (flex-1)
- **Card Grid**: grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6
