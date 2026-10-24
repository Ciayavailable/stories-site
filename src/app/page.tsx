import { Header } from "@/components/site/header";
import { Hero } from "@/components/site/hero";
import { About } from "@/components/site/about";
import { MenuSection } from "@/components/site/menu-section";
import { Features } from "@/components/site/features";
import { Contacts } from "@/components/site/contacts";
import { Footer } from "@/components/site/footer";

export default function Home() {
  return (
    <>
      <Header />
      <main>
        <Hero />
        <About />
        <MenuSection />
        <Features />
        <Contacts />
      </main>
      <Footer />
    </>
  );
}
