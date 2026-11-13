# G Tech — Auditoria visual das 6 mídias recebidas
Data: 13/11/2026
Analisados arquivos originais via Google Drive conectado, sem publicar mídias nem modificar o site em produção.

## Inventário técnico
| Arquivo | Duração | Resolução | Conteúdo observado | Uso recomendado |
|---|---:|---|---|---|
| ScreenRecording_08-03-2026 21-49-34_1.MP4 | 24,77s | 1170x2532 | Demonstração vertical de cardápio de restaurante, itens de comida e preços | Portfólio / estudos de caso de cardápio |
| ScreenRecording_08-06-2026 23-51-00_1.MP4 | 23,94s | 1170x2532 | Cardápio digital e fluxo de pedido/WhatsApp | Seção experiência do cliente / portfólio |
| IMG_1061.MOV | 36,06s | 1920x1080 | Plaquinhas NFC físicas, Google avaliações e Instagram, demonstração em mãos | Produto NFC e clipe hero curto |
| IMG_1069.MOV | 6,24s | 1920x1080 | Celular aproximado de uma placa NFC, mostrando experiência | Demonstração rápida, loop hero alternativo |
| IMG_1110.MOV | 34,67s | 1920x1080 | Demonstração da placa para avaliações do Google em celular | Seção como funciona e Reel instrutivo |
| IMG_1144.mov | 44,70s | 1080x1920 | Apresentador falando em ambiente interno, segurando celular | Vídeo explicativo/apresentação, condicionada a validação do contexto, consentimento e áudio |

## Seleção editorial sugerida
1. **Hero principal:** vídeo real curto (6–8s) cortado do `IMG_1061.MOV` ou `IMG_1069.MOV`, com legenda e CTA sobreposto; autoplay sem som, loop e fallback estático. Evitar informações de clientes legíveis nos quadros.
2. **Seção "NFC que aproxima":** `IMG_1110.MOV`, com versão curta otimizada e legenda descritiva de ação.
3. **Portfólio:** usar cada screen recording como preview da experiência digital. Não carregar os vídeos completos na home: abrir sob clique e lazy-load.
4. **Apresentação em vídeo:** `IMG_1144.mov`, depois de confirmar se pessoa retratada autorizou uso publicitário e se o conteúdo é sobre a G Tech.
5. **Reels:** fazer versão vertical de 15–25s com gancho, demonstração, benefício e CTA, sem afirmar taxa de conversão ou viralização garantidas.

## Políticas de mídia
- Direitos sobre conteúdo, trilha e imagem pessoal precisam ser checados. Evitar dados pessoais, prints de chats com clientes ou informação sensível.
- Fornecer compressão, poster e formatos compatíveis; testar mobile, rede lenta, acessibilidade e prefere-reduced-motion.
- A pasta de mídia original fica no Google Drive do proprietário; **não copiar vídeos para repositório GitHub público**.
- Preferir mídia em armazenamento/CDN apropriado, com controle de autorização e caching; CDN/domínio será definido após aprovação.

## Critério de aprovação
- Escolher o clipe de abertura; definir tom visual; aprovar layout e hierarquia.
- Criar protótipo isolado sem produção; CEO revisa; só depois criar implementação em branch de código, testes, preview e deploy autorizado.
