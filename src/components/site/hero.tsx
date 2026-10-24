'use client';

import { motion } from 'framer-motion';
import { Clock, MapPin, Star } from 'lucide-react';

export function Hero() {
  return (
    <section
      id="top"
      className="relative flex min-h-screen items-center justify-center overflow-hidden"
    >
      <div className="absolute inset-0">
        <img
          src="/images/hero.png"
          alt="Интерьер кафе Stories — столики у окна в вечернем свете"
          className="h-full w-full object-cover grayscale"
        />
        <div className="absolute inset-0 bg-black/60" />
        <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-black to-transparent" />
      </div>

      <motion.div
        initial={{ opacity: 0, y: 32 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: 'easeOut' }}
        className="relative z-10 mx-auto max-w-4xl px-4 text-center sm:px-6"
      >
        <p className="mb-6 flex flex-wrap items-center justify-center gap-x-3 gap-y-2 text-xs uppercase tracking-[0.3em] text-neutral-300 sm:text-sm">
          <span className="inline-flex items-center gap-1.5">
            <MapPin className="h-3.5 w-3.5" aria-hidden />
            Сочи · ул. Виноградная, 2/3
          </span>
          <span className="hidden text-neutral-600 sm:inline">·</span>
          <span className="inline-flex items-center gap-1.5">
            <Clock className="h-3.5 w-3.5" aria-hidden />
            Ежедневно до 22:00
          </span>
        </p>

        <h1 className="select-none text-7xl font-bold leading-none tracking-[0.06em] text-white sm:text-9xl md:text-[10rem]">
          STORIES
        </h1>

        <p className="mx-auto mt-8 max-w-xl text-lg leading-relaxed text-neutral-200 sm:text-xl">
          Кофейня с характером в центре Сочи.
          <br />
          Каждая история здесь начинается с чашки кофе.
        </p>

        <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
          <a
            href="#menu"
            className="w-full bg-white px-8 py-4 text-sm font-semibold uppercase tracking-widest text-black transition-colors hover:bg-neutral-200 sm:w-auto"
          >
            Смотреть меню
          </a>
          <a
            href="#contacts"
            className="w-full border border-white px-8 py-4 text-sm font-semibold uppercase tracking-widest text-white transition-colors hover:bg-white hover:text-black sm:w-auto"
          >
            Как добраться
          </a>
        </div>

        <div className="mt-12 inline-flex select-none items-center gap-3 border border-white/15 bg-black/40 px-5 py-3 backdrop-blur-sm">
          <span className="flex items-center gap-1" aria-hidden>
            {[...Array(5)].map((_, i) => (
              <Star key={i} className="h-4 w-4 fill-white text-white" />
            ))}
          </span>
          <span className="text-sm text-neutral-200">
            Рейтинг <strong className="font-semibold text-white">5.0</strong>
          </span>
        </div>
      </motion.div>
    </section>
  );
}
