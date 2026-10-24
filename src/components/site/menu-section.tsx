'use client';

import { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { MENU, type MenuItem, type MenuGroup } from '@/lib/menu-data';

function Price({ value }: { value: string }) {
  const isRange = value.includes('/');
  return (
    <span
      className={`whitespace-nowrap font-semibold text-white ${
        isRange ? 'text-base sm:text-lg' : 'text-xl sm:text-2xl'
      }`}
    >
      {value}
      <span className="ml-1 text-sm font-normal text-neutral-400">₽</span>
    </span>
  );
}

function ItemRow({ item }: { item: MenuItem }) {
  return (
    <li className="py-5">
      <div className="flex items-baseline gap-3">
        <h3 className="text-base font-medium text-white sm:text-lg">{item.name}</h3>
        {item.hit && (
          <span className="shrink-0 border border-white/30 px-2 py-0.5 text-[10px] uppercase tracking-widest text-neutral-300">
            Хит
          </span>
        )}
        {item.price && (
          <>
            <span
              className="mx-1 flex-1 -translate-y-1 border-b border-dotted border-white/25"
              aria-hidden
            />
            <Price value={item.price} />
          </>
        )}
      </div>
      {item.description && (
        <p className="mt-1.5 max-w-md text-sm leading-relaxed text-neutral-400">
          {item.description}
        </p>
      )}
    </li>
  );
}

function GroupBlock({ group }: { group: MenuGroup }) {
  return (
    <div>
      {group.title && (
        <h3 className="mb-2 mt-10 text-xs uppercase tracking-[0.25em] text-neutral-500 first:mt-0">
          {group.title}
        </h3>
      )}
      <ul className="divide-y divide-white/10">
        {group.items.map((item) => (
          <ItemRow key={`${group.title ?? 'list'}-${item.name}`} item={item} />
        ))}
      </ul>
    </div>
  );
}

export function MenuSection() {
  const [active, setActive] = useState(MENU[0].id);
  const [pageIndex, setPageIndex] = useState(0);
  const category = MENU.find((c) => c.id === active) ?? MENU[0];
  const pages = category.pages;
  const page = pages ? Math.min(pageIndex, pages.length - 1) : 0;
  const groups = pages ? pages[page].groups : category.groups;

  return (
    <section id="menu" className="bg-black text-white">
      <div className="mx-auto max-w-6xl px-4 py-20 sm:px-6 sm:py-28">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.6 }}
          className="text-center"
        >
          <p className="mb-4 text-xs uppercase tracking-[0.3em] text-neutral-500">
            Меню
          </p>
          <h2 className="text-4xl font-semibold tracking-tight sm:text-5xl">
            Что попробовать у нас
          </h2>
          <p className="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-neutral-400">
            Кофе и авторские рафы, завтраки, салаты, паста и домашние
            десерты. Цены указаны в рублях.
          </p>
        </motion.div>

        <div
          className="mt-12 flex flex-wrap justify-center gap-2 sm:gap-3"
          role="tablist"
          aria-label="Категории меню"
        >
          {MENU.map((c) => (
            <button
              key={c.id}
              role="tab"
              aria-selected={active === c.id}
              onClick={() => {
                setActive(c.id);
                setPageIndex(0);
              }}
              className={`min-h-11 px-4 py-2.5 text-sm uppercase tracking-widest transition-colors sm:px-5 ${
                active === c.id
                  ? 'bg-white text-black'
                  : 'border border-white/20 text-neutral-300 hover:border-white hover:text-white'
              }`}
            >
              {c.label}
            </button>
          ))}
        </div>

        {pages && (
          <div
            className="mt-4 flex flex-wrap justify-center gap-2"
            role="tablist"
            aria-label="Страницы категории"
          >
            {pages.map((p, i) => (
              <button
                key={p.label}
                role="tab"
                aria-selected={page === i}
                onClick={() => setPageIndex(i)}
                className={`min-h-9 px-3.5 py-2 text-xs uppercase tracking-widest transition-colors ${
                  page === i
                    ? 'bg-white text-black'
                    : 'border border-white/20 text-neutral-300 hover:border-white hover:text-white'
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        )}

        <AnimatePresence mode="wait">
          <motion.div
            key={`${category.id}-${page}`}
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.3 }}
            className="mx-auto mt-12 max-w-3xl"
          >
            {category.note && (
              <p className="mb-8 text-center text-sm text-neutral-500">
                {category.note}
              </p>
            )}
            {groups.map((group, gi) => (
              <GroupBlock key={group.title ?? `${category.id}-${page}-${gi}`} group={group} />
            ))}
          </motion.div>
        </AnimatePresence>
      </div>
    </section>
  );
}
