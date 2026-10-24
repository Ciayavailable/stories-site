'use client';

import { motion } from 'framer-motion';

const STATS = [
  { value: '5.0', label: 'рейтинг гостей' },
  { value: 'Сочи', label: 'ул. Виноградная, 2/3Б' },
  { value: '21:00', label: 'открыты ежедневно до' },
];

export function About() {
  return (
    <section id="about" className="bg-white text-black">
      <div className="mx-auto max-w-6xl px-4 py-20 sm:px-6 sm:py-28">
        <div className="mx-auto max-w-3xl">
          <div>
            <div className="overflow-hidden border border-neutral-200">
              <img
                src="/images/barista.png"
                alt="Бариста кафе Stories готовит фильтр-кофе"
                className="aspect-[3/2] w-full object-cover grayscale"
              />
            </div>
          </div>

          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: '-80px' }}
            transition={{ duration: 0.6 }}
            className="mt-12"
          >
            <p className="mb-4 text-xs uppercase tracking-[0.3em] text-neutral-500">
              О нас
            </p>
            <h2 className="text-4xl font-semibold tracking-tight sm:text-5xl">
              У каждой чашки —
              <br />
              своя история
            </h2>

            <div className="mt-8 space-y-5 text-base leading-relaxed text-neutral-600">
              <p>
                Stories — уютное кафе в самом сердце Сочи, в двух шагах от
                оживлённой Виноградной улицы. Мы верим, что хорошее место — это
                не только кофе и десерты, а люди, разговоры и моменты, которые
                хочется запомнить. Поэтому мы и назвались Stories: сюда
                приходят за утренним зарядом, тёплыми встречами и красивыми
                историями.
              </p>
              <p>
                Каждое утро наши бариста варят кофе на зерне, пекарь ставит
                свежие круассаны, а кухня готовит завтраки — от тёплых сырников
                со сметаной до зелёной гречки с яйцом пашот. А к кофе — витрина
                домашних десертов: медовик, меренговый рулет, птичье молоко и
                макаронс.
              </p>
              <p>
                Мы работаем ежедневно и открыты до 21:00 — так что за вечерним
                рафом или десертом тоже ждём именно вас.
              </p>
            </div>
          </motion.div>

          <div className="mt-12 grid gap-px border border-neutral-200 bg-neutral-200 sm:grid-cols-3">
            {STATS.map((stat) => (
              <div
                key={stat.value}
                className="flex flex-col items-center gap-1 bg-white px-6 py-8 text-center"
              >
                <span className="text-3xl font-bold tracking-tight">{stat.value}</span>
                <span className="text-xs uppercase tracking-widest text-neutral-500">
                  {stat.label}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
