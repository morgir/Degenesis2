/**
 * Instalator zawartości Degenesis 2.0: jednym przyciskiem przenosi kompendia do świata
 * (Dzienniki, Aktorzy, Sceny, Playlisty, Makra, Przedmioty) w uporządkowanych folderach, z uprawnieniami.
 */
import { SYSTEM_ID } from "../config.mjs";

const { DialogV2 } = foundry.applications.api;
const OBS = CONST.DOCUMENT_OWNERSHIP_LEVELS.OBSERVER;

/** Grupy instalacji. folder = nazwa folderu głównego w świecie; ownership = domyślny dostęp graczy. */
export const GROUPS = [
  { key: "gracze", label: "Podręcznik gracza i zasady", hint: "Dzienniki dla graczy (świat, regiony, kulty, zasady, PDF) — widoczne dla graczy.", checked: true,
    packs: [{ pack: "gracze", folder: "Degenesis 2.0 — dla graczy", ownership: OBS }, { pack: "zasady", folder: "Degenesis 2.0 — zasady", ownership: OBS }] },
  { key: "przygoda", label: "Przygoda „Ciche studnie”", hint: "Dzienniki MG i Szkoła MG, sceny z mapami, muzyka, NPC, frakcje, śledztwo, rejestr długów.", checked: true,
    packs: [{ pack: "przygoda", folder: "Ciche studnie" }, { pack: "sceny", folder: "Ciche studnie" }, { pack: "przyklady", folder: "Ciche studnie" }] },
  { key: "muzyka", label: "Odgłosy (deszcz, noc, podziemia, efekty)", hint: "Pętle tła i pojedyncze efekty na licencjach CC0/CC BY. Muzykę dodajesz własną.", checked: true,
    packs: [{ pack: "muzyka", folder: "Degenesis 2.0 — odgłosy" }] },
  { key: "postacie", label: "Gotowe postacie (7)", hint: "Widoczne dla graczy; przypisz je w Konfiguracji użytkownika.", checked: true,
    packs: [{ pack: "postacie", folder: "Gotowe postacie", ownership: OBS }] },
  { key: "przeciwnicy", label: "Przeciwnicy i bestiariusz", hint: "Ludzie, zwierzęta, Psychonauci — tylko dla MG.", checked: true,
    packs: [{ pack: "przeciwnicy", folder: "Przeciwnicy" }] },
  { key: "makra", label: "Makra MG", hint: "Kreator, wyrocznia, nowa sesja, obrażenia na cel.", checked: true,
    packs: [{ pack: "makra", folder: "Degenesis 2.0" }] },
  { key: "przedmioty", label: "Przedmioty (kultury, koncepty, kulty, potencjały, ekwipunek)", hint: "Niepotrzebne do gry — kreator czyta je z kompendiów. Zaznacz, jeśli chcesz je edytować w świecie.", checked: false,
    packs: ["kultury", "koncepty", "kulty", "potencjaly", "ekwipunek"].map(p => ({ pack: p, folder: "Degenesis 2.0" })) }
];

export function registerInstallerSettings() {
  game.settings.register(SYSTEM_ID, "installedVersion", { scope: "world", config: false, type: String, default: "" });
  game.settings.register(SYSTEM_ID, "showInstaller", { scope: "world", config: false, type: Boolean, default: true });
  game.settings.registerMenu(SYSTEM_ID, "installerMenu", {
    name: "Instalator zawartości", label: "Otwórz instalator", hint: "Importuje zasady, przygodę, postacie i przeciwników z kompendiów do świata.",
    icon: "fa-solid fa-box-open", type: InstallerMenu, restricted: true
  });
}

/** Klasa „menu” dla ustawień: zamiast okna otwiera dialog instalatora. */
class InstallerMenu extends foundry.applications.api.ApplicationV2 {
  async render() { openInstaller(); return this; }
}

export function checkInstaller() {
  if (!game.user.isGM) return;
  const installed = game.settings.get(SYSTEM_ID, "installedVersion");
  const current = game.system.version;
  if (!installed && game.settings.get(SYSTEM_ID, "showInstaller")) return openInstaller();
  if (installed && foundry.utils.isNewerVersion(current, installed)) return openInstaller({ update: installed });
}

export async function openInstaller({ update = null } = {}) {
  const rows = GROUPS.map(g => {
    const n = g.packs.reduce((t, p) => t + (game.packs.get(`${SYSTEM_ID}.${p.pack}`)?.index.size ?? 0), 0);
    return `<label class="d2-inst-row"><input type="checkbox" name="${g.key}" ${g.checked ? "checked" : ""}>
      <span><b>${g.label}</b> <span class="d2-inst-n">(${n})</span><br><small>${g.hint}</small></span></label>`;
  }).join("");
  const intro = update
    ? `<p>System zaktualizowano z wersji <b>${update}</b> do <b>${game.system.version}</b>. Możesz doinstalować nową zawartość — istniejące dokumenty zostaną pominięte albo, jeśli zaznaczysz opcję niżej, nadpisane wersją z kompendium.</p>`
    : `<p>Witaj w <b>Degenesis 2.0</b>. Zaznacz, co przenieść z kompendiów do świata. Wszystko trafi do osobnych folderów, a dokumenty dla graczy dostaną od razu prawo podglądu.</p>`;
  const content = `<div class="d2-installer">${intro}${rows}
    <hr><label class="d2-inst-row"><input type="checkbox" name="overwrite"><span>Nadpisz dokumenty, które już są w świecie <small>(utracisz własne zmiany w nich)</small></span></label>
    <label class="d2-inst-row"><input type="checkbox" name="activate" ${update ? "" : "checked"}><span>Aktywuj scenę startową i otwórz Szkołę MG</span></label></div>`;
  const choice = await DialogV2.wait({
    window: { title: "Degenesis 2.0 — instalator zawartości", icon: "fa-solid fa-box-open" },
    position: { width: 560 },
    content,
    buttons: [
      { action: "install", label: "Zainstaluj", icon: "fa-solid fa-download", default: true,
        callback: (event, button) => Object.fromEntries([...button.form.elements].filter(e => e.name).map(e => [e.name, e.checked])) },
      { action: "later", label: "Później", icon: "fa-solid fa-clock" },
      { action: "never", label: "Nie pokazuj więcej", icon: "fa-solid fa-xmark" }
    ],
    rejectClose: false
  });
  if (choice === "never") {
    await game.settings.set(SYSTEM_ID, "showInstaller", false);
    await game.settings.set(SYSTEM_ID, "installedVersion", game.system.version);
    return ui.notifications.info("Instalator znajdziesz w Ustawieniach → Konfiguracja gry → Degenesis 2.0.");
  }
  if (!choice || choice === "later") return;
  return installContent(choice);
}

export async function installContent(opts) {
  const notice = ui.notifications.info("Degenesis 2.0: instaluję zawartość…", { permanent: true });
  const summary = [];
  try {
    for (const g of GROUPS) {
      if (!opts[g.key]) continue;
      let n = 0;
      for (const p of g.packs) n += await importPack(p, opts.overwrite);
      summary.push(`${g.label}: ${n}`);
    }
    await game.settings.set(SYSTEM_ID, "installedVersion", game.system.version);
    await game.settings.set(SYSTEM_ID, "showInstaller", false);
    if (opts.activate) await activateStart();
  } catch (err) {
    console.error(`${SYSTEM_ID} | instalator`, err);
    ui.notifications.error(`Instalacja przerwana: ${err.message}`);
  } finally {
    notice?.remove?.();
  }
  if (summary.length) ui.notifications.info(`Zainstalowano — ${summary.join("; ")}.`);
}

/** Folder w świecie (tworzy, jeśli go brak). */
async function ensureFolder(name, type, parent = null, extra = {}) {
  const found = game.folders.find(f => f.type === type && f.name === name && (f.folder?.id ?? null) === parent);
  if (found) return found;
  return Folder.create({ name, type, folder: parent, color: "#7b1e12", sorting: "m", ...extra });
}

/** Import jednego kompendium z zachowaniem struktury folderów i ID. Zwraca liczbę zaimportowanych dokumentów. */
async function importPack({ pack: name, folder: rootName, ownership }, overwrite) {
  const pack = game.packs.get(`${SYSTEM_ID}.${name}`);
  if (!pack) { console.warn(`${SYSTEM_ID} | brak kompendium ${name}`); return 0; }
  const type = pack.documentName;
  const collection = game.collections.get(type);
  const root = await ensureFolder(rootName, type);

  // Odtwórz foldery z kompendium pod folderem głównym
  const fmap = {};
  const folders = [...(pack.folders ?? [])].sort((a, b) => (a.ancestors?.length ?? 0) - (b.ancestors?.length ?? 0));
  for (const f of folders) {
    const parentId = f.folder ? fmap[f.folder.id ?? f.folder] : root.id;
    const wf = await ensureFolder(f.name, type, parentId ?? root.id, { color: f.color ?? "#7b1e12", sort: f.sort });
    fmap[f.id] = wf.id;
  }

  const docs = await pack.getDocuments();
  const create = [], update = [];
  for (const doc of docs) {
    const data = collection.fromCompendium(doc, { keepId: true, clearFolder: true, clearOwnership: true });
    const src = doc._source.folder;
    data.folder = (src && fmap[src]) || root.id;
    if (ownership && !/^Dla MG/.test(doc.name)) data.ownership = { default: ownership };
    if (collection.has(doc.id)) { if (overwrite) update.push(data); }
    else create.push(data);
  }
  const cls = CONFIG[type].documentClass;
  if (create.length) await cls.createDocuments(create, { keepId: true });
  if (update.length) {
    // nadpisanie = usuń i utwórz od nowa (embedded: przedmioty aktorów, strony dzienników, dźwięki)
    await cls.deleteDocuments(update.map(d => d._id));
    await cls.createDocuments(update, { keepId: true });
  }
  return create.length + update.length;
}

async function activateStart() {
  const scene = game.scenes.find(s => s.name.startsWith("Justitian"));
  if (scene) {
    await scene.update({ navigation: true });
    await scene.activate();
  }
  for (const s of game.scenes.filter(s => s.folder?.name === "Ciche studnie")) if (!s.navigation) await s.update({ navigation: true });
  const school = game.journal.find(j => j.name.startsWith("Szkoła MG"));
  school?.sheet?.render(true);
}
