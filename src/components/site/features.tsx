'use client';

import { motion } from 'framer-motion';
import {
  CakeSlice,
  Clock,
  Coffee,
  MapPin,
  Milk,
} from 'lucide-react';

/** Стопка сырников — кастомная иконка в стиле lucide */
function SyrnikiIcon({ className }: { className?: string }) {
  return (
    <svg
      className={className}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden
    >
      <ellipse cx="12" cy="5.5" rx="7.5" ry="2.8" />
      <path d="M4.5 5.5v3.2c0 1.55 3.36 2.8 7.5 2.8s7.5-1.25 7.5-2.8V5.5" />
      <path d="M4.5 8.7v3.2c0 1.55 3.36 2.8 7.5 2.8s7.5-1.25 7.5-2.8V8.7" />
      <path d="M4.5 11.9v3.6c0 1.55 3.36 2.8 7.5 2.8s7.5-1.25 7.5-2.8v-3.6" />
    </svg>
  );
}

const FEATURES = [
  {
    icon: Coffee,
    title: 'Кофе на зерне',
    text: 'Классика, фильтр и авторские рафы — от медового и лавандового до «дубайского шоколада».',
  },
  {
    icon: SyrnikiIcon,
    title: 'Завтраки',
    text: 'Сырники, шакшука, скрэмбл и зелёная гречка — заказывайте к открытию и к самому закрытию.',
  },
  {
    icon: CakeSlice,
    title: 'Домашние десерты',
    text: 'Медовик, меренговый рулет, чизкейк и макаронс — витрина обновляется каждый день.',
  },
  {
    icon: Milk,
    title: 'Растительное молоко',
    text: 'Капучино, латте и моккочино готовим на кокосовом, банановом и миндальном молоке.',
  },
  {
    icon: Clock,
    title: 'Открыты до 21:00',
    text: 'Ежедневно, без выходных — заходите на завтрак, обеденный кофе или вечерний десерт.',
  },
  {
    icon: MapPin,
    title: 'Центр Сочи',
    text: 'Виноградная, 2/3Б — в двух шагах от оживлённой улицы, рядом удобная парковка.',
  },
];

export function Features() {
  return (
    <section id="features" className="bg-white text-black">
      <div className="mx-auto max-w-6xl px-4 py-20 sm:px-6 sm:py-28">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.6 }}
          className="mb-12 text-center"
        >
          <p className="mb-4 text-xs uppercase tracking-[0.3em] text-neutral-500">
            Почему мы
          </p>
          <h2 className="text-4xl font-semibold tracking-tight sm:text-5xl">
            Заходите и проверяйте
          </h2>
        </motion.div>

        <div className="grid gap-px border border-neutral-200 bg-neutral-200 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map((feature) => (
            <div
              key={feature.title}
              className="flex flex-col gap-3 bg-white px-6 py-10 text-center sm:px-8"
            >
              <feature.icon
                className="mx-auto mb-1 h-6 w-6 text-neutral-400"
                aria-hidden
              />
              <h3 className="text-lg font-semibold">{feature.title}</h3>
              <p className="text-sm leading-relaxed text-neutral-600">
                {feature.text}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
