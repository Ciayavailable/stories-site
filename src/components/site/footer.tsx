export function Footer() {
  return (
    <footer className="mt-auto border-t border-white/10 bg-black text-white">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-4 px-4 py-10 text-center sm:flex-row sm:justify-between sm:px-6 sm:text-left">
        <p className="select-none text-xl font-bold tracking-widest">STORIES</p>
        <p className="text-sm text-neutral-500">
          © {new Date().getFullYear()} Кафе «Stories» · Сочи, ул. Виноградная, 2/3Б
        </p>
        <p className="text-sm text-neutral-500">
          Сделано с любовью к кофе
        </p>
      </div>
    </footer>
  );
}
