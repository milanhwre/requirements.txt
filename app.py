"from flask import Flask, render_template_string
app = Flask(__name__)
# HTML template as a multi-line string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Black Alliance</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            background-image: url('https://via.placeholder.com/1920x1080'); /* Placeholder for background image */
            background-size: cover;
        }
        .text-primary {
            color: #1d4ed8; /* Example primary color */
        }
    </style>
</head>
<body>
    <nav class="navbar p-4 shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <div class="text-2xl text-primary">Black Alliance ♚</div>
            <div class="hidden lg:flex navbar-menu">
                <a href="/" class="hover:text-primary">Home</a>
                <a href="/team" class="hover:text-primary">Team</a>
                <a href="/services" class="hover:text-primary">Services</a>
                <a href="/status" class="hover:text-primary">Status</a>
                <a href="/pricing" class="hover:text-primary">Pricing</a>
                <a href="/contact" class="hover:text-primary">Contact</a>
            </div>
            <div class="lg:hidden">
                <span id="menu-btn" class="navbar-icon text-2xl">
                    <i class="fas fa-bars"></i>
                </span>
            </div>
        </div>
    </nav>
    <header class="bg-header shadow-lg flex items-center justify-center text-center"></header>
    <div class="container mx-auto px-4 py-16">
        <section id="cards">
            <h2 class="text-3xl font-bold text-center text-primary mb-8">𝘖𝘶𝘳 𝘖𝘧𝘧𝘦𝘳𝘪𝘯𝘨𝘴</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bg-white rounded-lg shadow-lg p-6 text-center">
                    <div class="card-img mb-4">
                        <img src="https://via.placeholder.com/150" alt="Services Image">
                    </div>
                    <h3 class="text-2xl font-bold text-primary mb-4">𝘚𝘦𝘳𝘷𝘪𝘤𝘦𝘴</h3>
                    <a href="/services" class="mt-4 inline-block px-6 py-2 bg-blue-500 text-white rounded-lg">View</a>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6 text-center">
                    <div class="card-img mb-4">
                        <img src="https://via.placeholder.com/150" alt="Teams Image">
                    </div>
                    <h3 class="text-2xl font-bold text-primary mb-4">𝘛𝘦𝘢𝘮</h3>
                    <a href="/team" class="mt-4 inline-block px-6 py-2 bg-blue-500 text-white rounded-lg">View</a>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6 text-center">
                    <div class="card-img mb-4">
                        <img src="https://via.placeholder.com/150" alt="Pricing Image">
                    </div>
                    <h3 class="text-2xl font-bold text-primary mb-4">𝘗𝘳𝘪𝘤𝘪𝘯𝘨</h3>
                    <a href="/pricing" class="mt-4 inline-block px-6 py-2 bg-blue-500 text-white rounded-lg">View</a>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6 text-center">
                    <div class="card-img"
 https://chat.two.ai/#:~:text=in%20One%20Script-,from,-flask
