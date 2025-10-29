
import { StartScreenPrompt } from "@openai/chatkit";

export const CHATKIT_API_URL =
  import.meta.env.VITE_CHATKIT_API_URL ?? "/chatkit";

/**
 * ChatKit still expects a domain key at runtime. Use any placeholder locally,
 * but register your production domain at
 * https://platform.openai.com/settings/organization/security/domain-allowlist
 * and deploy the real key.
 */
export const CHATKIT_API_DOMAIN_KEY =
  import.meta.env.VITE_CHATKIT_API_DOMAIN_KEY ?? "domain_pk_localhost_dev";

export const FACTS_API_URL = import.meta.env.VITE_FACTS_API_URL ?? "/facts";

export const THEME_STORAGE_KEY = "chatkit-boilerplate-theme";

export const GREETING = "GhostCrew Agent Initialized. Awaiting Directives.";

export const STARTER_PROMPTS: StartScreenPrompt[] = [
  {
    label: "Scan a target",
    prompt: "scan example.com with nmap",
    icon: "search",
  },
  {
    label: "Fuzz a URL",
    prompt: "scan http://example.com with ffuf wordlist wordlist.txt",
    icon: "search",
  },
  {
    label: "Check for SQLi",
    prompt: "scan http://testphp.vulnweb.com/listproducts.php?cat=1 with sqlmap",
    icon: "search",
  },
  {
    label: "List files in workspace",
    prompt: "list files in workspace",
    icon: "book-open",
  },
];

export const PLACEHOLDER_INPUT = "Enter command...";
