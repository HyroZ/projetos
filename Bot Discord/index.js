require("dotenv").config();

const { 
  Client,
  GatewayIntentBits,
  Events
} = require("discord.js");

const { GoogleGenerativeAI } = require("@google/generative-ai");

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

const genAI = new GoogleGenerativeAI(
  process.env.GEMINI_API_KEY
);

const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash"
});

client.once(Events.ClientReady, () => {
  console.log("Bot online!");
});

client.on(Events.MessageCreate, async (message) => {

  if (message.author.bot) return;

  if (!message.content.startsWith("!")) return;

  const pergunta = message.content.slice(1);

  try {

    await message.channel.sendTyping();

    const result = await model.generateContent(pergunta);

    const response = await result.response;

    const text = response.text();

    message.reply(text);

  } catch (error) {

    console.error("ERRO COMPLETO:", error);

    message.reply("Erro na IA.");

  }

});

client.login(process.env.DISCORD_TOKEN);