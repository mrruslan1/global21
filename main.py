from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  


messages = []

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        
        if not name or not email or not message:
            flash('Пожалуйста, заполните все поля!', 'error')
        else:
            
            messages.append({
                'name': name,
                'email': email,
                'message': message
            })
            flash('Сообщение успешно отправлено!', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
