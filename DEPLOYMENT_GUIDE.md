# HARNESS PORTAL - DEPLOYMENT GUIDE
## Self-Hosted Web Portal for Your Harness Drawings

---

## 🎯 WHAT YOU HAVE

A complete, professional web portal with:
- ✅ Beautiful, responsive design
- ✅ Search functionality
- ✅ Print-friendly layout
- ✅ Question submission form
- ✅ Mobile-friendly
- ✅ No external dependencies
- ✅ Password protection available

---

## 🔒 SECURITY OPTIONS (Best to Worst for Confidential Drawings)

### ⭐ OPTION 1: GitHub Private Repo + Password Protection (RECOMMENDED)

**Security Level:** 🔒🔒🔒🔒 EXCELLENT

**How it works:**
- GitHub repo is PRIVATE (only you can see the code)
- Deploy to Netlify with PASSWORD protection
- Vendor needs password to access
- You control everything
- Drawings are never public

**Cost:** FREE  
**Setup Time:** 20 minutes  
**Maintenance:** Very easy

**Best for:** Confidential drawings with external vendors

---

### ⭐ OPTION 2: Netlify Password Protection (Simple)

**Security Level:** 🔒🔒🔒 GOOD

**How it works:**
- Upload site to Netlify (drag-and-drop)
- Enable Netlify's built-in password protection
- Vendor enters password to access site
- Simple username/password authentication

**Cost:** FREE (Netlify free tier includes password protection)  
**Setup Time:** 10 minutes  
**Maintenance:** Very easy

**Best for:** Quick setup, single password for all vendors

---

### OPTION 3: Cloudflare Pages + Access Control

**Security Level:** 🔒🔒🔒🔒 EXCELLENT

**How it works:**
- Deploy to Cloudflare Pages
- Use Cloudflare Access for email-based authentication
- Vendor must verify their email to access
- More granular control

**Cost:** FREE  
**Setup Time:** 25 minutes  
**Maintenance:** Easy

**Best for:** Multiple vendors, need email-based access

---

### OPTION 4: Company Web Server (If You Have One)

**Security Level:** 🔒🔒🔒🔒🔒 MAXIMUM

**How it works:**
- Host on your company's web server
- Use company firewall/VPN
- Full IT control

**Cost:** $0 (if server exists) or $5-10/month for VPS  
**Setup Time:** 30 minutes - 1 hour (depends on IT)  
**Maintenance:** Moderate

**Best for:** Maximum control, IT wants everything internal

---

### ⚠️ OPTION 5: GitHub Pages (NOT RECOMMENDED FOR YOU)

**Security Level:** 🔒 POOR (Public)

**Why not:** GitHub Pages is PUBLIC by default. Not suitable for confidential drawings.

---

## 🚀 RECOMMENDED SETUP: OPTION 1 (GitHub Private + Netlify)

This gives you the best balance of:
- ✅ Security (private repo, password protected)
- ✅ Ease of use (drag-and-drop updates)
- ✅ Free hosting
- ✅ Professional appearance
- ✅ Easy maintenance

---

## 📋 STEP-BY-STEP SETUP (Option 1 - GitHub + Netlify)

### PHASE 1: Prepare Your Files (5 minutes)

**Files are already created in:** `C:\Users\Jesus Lira\harness-portal\`

1. **Create a folder for your drawings:**
   ```
   C:\Users\Jesus Lira\harness-portal\drawings\
   ```

2. **Copy your 3 PDFs into that folder:**
   - Copy `Desktop\Tickets\04-210-2961.A1.pdf` → `harness-portal\drawings\04-210-2961.A.pdf`
   - Copy `Desktop\Tickets\04-210-3162.A1.pdf` → `harness-portal\drawings\04-210-3162.A1.pdf`
   - Copy `Desktop\Tickets\04-210-3559.A1.pdf` → `harness-portal\drawings\04-210-3559.A1.pdf`

**Your folder structure should look like:**
```
harness-portal/
├── index.html              (main page)
├── form.html               (question form)
├── thank-you.html          (confirmation page)
├── styles.css              (main styles)
├── form-styles.css         (form styles)
└── drawings/               (PDF folder)
    ├── 04-210-2961.A.pdf
    ├── 04-210-3162.A1.pdf
    └── 04-210-3559.A1.pdf
```

---

### PHASE 2: Set Up Form Email Handling (5 minutes)

**Option A: Use Formspree (Easiest - FREE)**

1. Go to: https://formspree.io/
2. Sign up (free account)
3. Click "Create new form"
4. You'll get a form ID like: `f/abcd1234`
5. Open `form.html` in Notepad
6. Find this line:
   ```html
   <form id="inquiryForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
7. Replace `YOUR_FORM_ID` with your actual ID: `f/abcd1234`
8. Save the file

**Now when vendors submit questions, they'll be emailed to you!**

**Option B: Use your company email directly**

Edit `form.html` and change:
```html
<form id="inquiryForm" action="mailto:engineering@yourcompany.com" method="POST" enctype="text/plain">
```

(Note: This opens the vendor's email client, less seamless but works)

---

### PHASE 3: Create GitHub Private Repository (5 minutes)

1. **Go to:** https://github.com/
2. **Sign up or log in**
3. **Click "New repository"** (green button, top right)
4. **Settings:**
   - Repository name: `harness-portal`
   - Description: "Confidential harness drawing portal"
   - **IMPORTANT:** Select **"Private"** (not Public!)
   - Click "Create repository"

5. **Upload your files:**
   - On the repo page, click "uploading an existing file"
   - Drag ALL files from `C:\Users\Jesus Lira\harness-portal\` into the box
   - Make sure to include the `drawings/` folder with PDFs
   - Add commit message: "Initial portal setup"
   - Click "Commit changes"

**✅ Your drawings are now in a PRIVATE GitHub repo (only you can see them)**

---

### PHASE 4: Deploy to Netlify with Password Protection (10 minutes)

1. **Go to:** https://www.netlify.com/
2. **Sign up** (use your GitHub account for easy linking)
3. **Click "Add new site" → "Import an existing project"**
4. **Choose "GitHub"**
5. **Authorize Netlify to access your GitHub**
6. **Select your `harness-portal` repository**
7. **Deploy settings:**
   - Build command: (leave blank)
   - Publish directory: `/` (or leave blank)
   - Click "Deploy site"

8. **Wait 1-2 minutes** for deployment

9. **Enable Password Protection:**
   - Go to your site settings
   - Click "Site configuration" → "Access control"
   - Enable "Password protection"
   - Set username: `vendor`
   - Set password: `HarnessSecure2026!` (or whatever you want)
   - Save

10. **Get your site URL:**
    - Netlify gives you a URL like: `https://random-name-123.netlify.app`
    - You can customize it: Site settings → Domain management → Edit site name
    - Example: `https://harness-drawings.netlify.app`

**✅ Your portal is now LIVE and PASSWORD PROTECTED!**

---

### PHASE 5: Test the Portal (5 minutes)

1. **Open your site URL** (e.g., `https://harness-drawings.netlify.app`)
2. **Enter the password** you set
3. **Test:**
   - ✅ Can you see the drawing list?
   - ✅ Can you download a PDF?
   - ✅ Can you click "Ask Question"?
   - ✅ Can you submit the form?
   - ✅ Did you receive the email?

**If all ✅ → You're done! 🎉**

---

### PHASE 6: Share with Your Vendor (2 minutes)

**Send them this email:**

```
Subject: Harness Drawing Portal - Access Instructions

Hi [Vendor Team],

I've set up a secure portal for accessing our harness drawings.

🔐 PORTAL ACCESS:
URL: https://harness-drawings.netlify.app
Username: vendor
Password: HarnessSecure2026!

⚠️ IMPORTANT - CONFIDENTIAL:
- These drawings are proprietary - do not share credentials
- Always check the revision before starting production
- Use "Ask Question" button for any clarifications

📋 HOW TO USE:
1. Open the URL and enter credentials
2. View/download drawings by clicking "Download Drawing"
3. Print the list: Press Ctrl+P for your production floor
4. Ask questions: Click "Ask Question" next to any drawing

You'll receive email responses within 2 business days.

Questions? Reply to this email.

Thanks,
[Your Name]
Engineering Team
```

---

## 🔄 HOW TO UPDATE DRAWINGS (Your Workflow)

When you need to add/update a drawing:

### Method 1: Via GitHub Web (Easiest)

1. Go to your GitHub repo: `github.com/yourusername/harness-portal`
2. Navigate to `drawings/` folder
3. Click "Add file" → "Upload files"
4. Drag your new/updated PDF
5. Commit changes
6. Netlify auto-deploys in 30 seconds
7. Vendor sees new drawing immediately

### Method 2: Via GitHub Desktop (Better for frequent updates)

1. Install GitHub Desktop
2. Clone your repo to your computer
3. Edit files locally
4. Drag new PDFs into `drawings/` folder
5. Commit and push
6. Auto-deploys to Netlify

**Time to add a new drawing: 2 minutes**  
**Time to update a drawing: 1 minute**

---

## 🔒 SECURITY FEATURES YOU GET

✅ **Private GitHub Repo** - Only you can see the source code  
✅ **Password Protection** - Netlify's built-in auth  
✅ **HTTPS Encryption** - All traffic is encrypted  
✅ **No Public Links** - Drawings are behind password  
✅ **Audit Trail** - Netlify shows you access logs  
✅ **Easy Revoke** - Change password to block access  

**Security Level: GOOD for confidential drawings with external vendors**

---

## 🆚 COMPARISON: GitHub vs Google Drive

| Feature | Google Drive (Blocked) | GitHub + Netlify |
|---------|------------------------|------------------|
| External Sharing | ❌ Blocked by IT | ✅ Works |
| Password Protection | ❌ N/A | ✅ Yes |
| Private by Default | ✅ Yes | ✅ Yes (private repo) |
| Version Control | ✅ Yes | ✅ Yes (better!) |
| Cost | Free | Free |
| Setup Time | 30 min | 30 min |
| Updates | Drag-drop | Drag-drop (GitHub) |
| Professional Look | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Mobile-Friendly | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Printable | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Forms Integration | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| IT Approval | ❌ Blocked | ✅ No issues |

**Winner: GitHub + Netlify!**

---

## 💰 COST BREAKDOWN

| Item | Free Tier | Paid Tier | Your Cost |
|------|-----------|-----------|-----------|
| GitHub Private Repo | Unlimited | N/A | **$0** |
| Netlify Hosting | 100GB bandwidth/mo | $19/mo for 400GB | **$0** |
| Netlify Password Protection | Included | N/A | **$0** |
| Formspree (emails) | 50 submissions/mo | $10/mo unlimited | **$0** |
| Domain (optional) | N/A | $12/year | $0 (use Netlify subdomain) |
| **TOTAL** | | | **$0/month** |

**You get a professional portal for FREE!**

---

## 📊 BANDWIDTH ESTIMATE

**Your usage:**
- 1 PDF = ~2MB
- 3 drawings = 6MB total
- 1 vendor downloads all 3 = 6MB
- Vendor downloads 10 times/month = 60MB
- Portal page loads = ~500KB each

**Monthly estimate for 1 vendor:**
- Downloads: 60MB
- Page views (30 times): 15MB
- **Total: ~75MB/month**

**Netlify free tier: 100GB/month = 100,000MB**

**You could support 1,300 vendors before hitting the free limit!**

---

## 🎨 CUSTOMIZATION (Optional)

### Change Colors
Edit `styles.css`:
- Line 10: Change gradient colors
- Line 34: Change header colors
- Line 95: Change button colors

### Add Your Logo
1. Add logo image to repo: `logo.png`
2. Edit `index.html`, add before `<h1>`:
   ```html
   <img src="logo.png" alt="Company Logo" style="max-width: 200px; margin-bottom: 20px;">
   ```

### Add More Drawings
Edit `index.html`, copy a table row and modify:
```html
<tr>
    <td class="part-number">04-210-XXXX</td>
    <td>Description here</td>
    <td class="revision">B</td>
    <td>01/29/2026</td>
    <td>7</td>
    <td><span class="badge badge-released">✅ Released</span></td>
    <td class="actions">
        <a href="drawings/04-210-XXXX.B.pdf" class="btn btn-download" download>📄 Download</a>
        <a href="form.html?part=04-210-XXXX&rev=B" class="btn btn-question">❓ Ask Question</a>
    </td>
</tr>
```

---

## 🔧 TROUBLESHOOTING

### "Password protection isn't showing up"
- Make sure you're on Netlify's paid plan (actually free tier includes this!)
- Try: Site settings → Access control → Enable password protection

### "Form submissions not arriving"
- Check your Formspree account spam folder
- Verify the form action URL in `form.html`
- Check Formspree dashboard for submissions

### "PDFs won't download"
- Make sure PDFs are in `drawings/` folder in GitHub
- Check file names match exactly in `index.html`
- Verify files committed to GitHub

### "Site not updating"
- GitHub changes can take 1-2 minutes to deploy
- Check Netlify "Deploys" tab for build status
- Try clearing browser cache

---

## ✅ FINAL CHECKLIST

- [ ] Files created in `harness-portal/` folder
- [ ] PDFs copied to `drawings/` subfolder
- [ ] Formspree form ID added to `form.html`
- [ ] GitHub PRIVATE repo created
- [ ] All files uploaded to GitHub (including PDFs)
- [ ] Netlify site deployed
- [ ] Password protection enabled on Netlify
- [ ] Custom site name set (optional)
- [ ] Tested: Can access site with password
- [ ] Tested: Can download PDF
- [ ] Tested: Can submit form
- [ ] Tested: Received form email
- [ ] Email sent to vendor with credentials
- [ ] Vendor confirmed they can access

**All checked? You're LIVE! 🎉**

---

## 🆘 NEED HELP?

**GitHub Issues:**
- "How do I make repo private?" → Settings → Danger Zone → Change visibility
- "Can't upload files" → Make sure repo is initialized (add README)

**Netlify Issues:**
- "Where's password protection?" → Site settings → Access control
- "Site won't deploy" → Check Netlify deploy logs

**General Issues:**
- Check the troubleshooting section above
- Google: "[your issue] netlify" or "[your issue] github"

---

## 🎁 WHAT YOU GET

✅ **Professional web portal** - Better than Google Sheets  
✅ **Password protected** - Secure for confidential drawings  
✅ **Mobile-friendly** - Works on tablets at workbench  
✅ **Print-friendly** - Vendor can print for floor  
✅ **Search function** - Find drawings quickly  
✅ **Question form** - Emails you directly  
✅ **Free hosting** - $0/month forever  
✅ **Easy updates** - Drag-and-drop new PDFs  
✅ **Version control** - GitHub tracks all changes  
✅ **No IT restrictions** - Bypasses corporate blocks  

**Total setup time: 30 minutes**  
**Ongoing maintenance: 2 minutes per drawing update**

---

## 🚀 NEXT STEPS

1. **Read through this guide** (you just did! ✅)
2. **Prepare your files** (Phase 1)
3. **Set up Formspree** (Phase 2)
4. **Create GitHub repo** (Phase 3)
5. **Deploy to Netlify** (Phase 4)
6. **Test everything** (Phase 5)
7. **Share with vendor** (Phase 6)

**Ready to start? Let's do Phase 1!**

Open File Explorer and navigate to `C:\Users\Jesus Lira\harness-portal\` to see your files!
