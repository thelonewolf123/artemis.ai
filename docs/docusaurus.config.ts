import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "Artemis AI",
  tagline: "A Practical Guide to Building Agentic AI Systems",
  favicon: "img/favicon.ico",

  future: {
    v4: true
  },

  url: "https://artemis-ai.dev",
  baseUrl: "/",

  organizationName: "artemis-ai",
  projectName: "artemis.ai",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"]
  },

  markdown: {
    mermaid: true
  },

  themes: ["@docusaurus/theme-mermaid"],

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          routeBasePath: "/"
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css"
        }
      } satisfies Preset.Options
    ]
  ],

  themeConfig: {
    image: "img/artemis-social-card.jpg",
    colorMode: {
      defaultMode: "light",
      disableSwitch: false,
      respectPrefersColorScheme: true
    },
    mermaid: {
      theme: { light: "neutral", dark: "dark" }
    },
    navbar: {
      title: "Artemis AI",
      logo: {
        alt: "Artemis AI Logo",
        src: "img/logo.svg"
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Documentation"
        },
        {
          href: "https://github.com/thelonewolf123/artemis.ai",
          label: "GitHub",
          position: "right"
        }
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Learn",
          items: [
            {
              label: "Getting Started",
              to: "/getting-started/installation"
            },
            {
              label: "Understanding LLMs",
              to: "/understanding-llms"
            }
          ]
        },
        {
          title: "Build",
          items: [
            {
              label: "Building Agents",
              to: "/building-agents"
            },
            {
              label: "Memory Management",
              to: "/memory-management"
            }
          ]
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/thelonewolf123/artemis.ai"
            }
          ]
        }
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Artemis AI. Built with Docusaurus.`
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ["bash", "json", "python"]
    }
  } satisfies Preset.ThemeConfig
};

export default config;
