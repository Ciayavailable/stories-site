'use client';

import { motion } from 'framer-motion';
import { Clock, MapPin, Star } from 'lucide-react';

const MAPS_URL = `https://yandex.ru/maps/?text=${encodeURIComponent(
  'Сочи, улица Виноградная 2/3'
)}`;

const CARDS = [
  {
    icon: MapPin,
    title: 'Адрес',
    lines: ['г. Сочи, ул. Виноградная, 2/3'],
  },
  {
    icon: Clock,
    title: 'Часы работы',
    lines: ['Ежедневно', 'Открыто до 22:00'],
  },
  {
    icon: Star,
    title: 'Рейтинг гостей',
    lines: ['5 из 5 — оценок «отлично»'],
  },
];

export function Contacts() {
  return (
    <section id="contacts" className="bg-black text-white">
      <div className="mx-auto max-w-6xl px-4 py-20 sm:px-6 sm:py-28">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.6 }}
          className="text-center"
        >
          <p className="mb-4 text-xs uppercase tracking-[0.3em] text-neutral-500">
            Контакты
          </p>
          <h2 className="text-4xl font-semibold tracking-tight sm:text-5xl">
            Ждём вас в гостях
          </h2>
        </motion.div>

        <div className="mt-12 grid gap-px border border-white/10 bg-white/10 sm:grid-cols-3">
          {CARDS.map((card) => (
            <div
              key={card.title}
              className="flex flex-col items-center gap-2 bg-black px-6 py-10 text-center"
            >
              <card.icon className="mb-2 h-5 w-5 text-neutral-500" aria-hidden />
              <h3 className="text-sm uppercase tracking-widest text-neutral-400">
                {card.title}
              </h3>
              {card.lines.map((line) => (
                <p key={line} className="text-base text-white">
                  {line}
                </p>
              ))}
            </div>
          ))}
        </div>

        <div className="mt-12 text-center">
          <a
            href={MAPS_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 bg-white px-8 py-4 text-sm font-semibold uppercase tracking-widest text-black transition-colors hover:bg-neutral-200"
          >
            <MapPin className="h-4 w-4" aria-hidden />
            Открыть в Яндекс Картах
          </a>
          <p className="mt-6 text-sm text-neutral-500">
            Центр Сочи, удобная парковка рядом — заходите на кофе, завтрак или
            десерт после моря.
          </p>
        </div>
      </div>
    </section>
  );
}
