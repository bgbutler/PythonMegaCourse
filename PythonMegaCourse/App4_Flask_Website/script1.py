from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")



@app.route('/plot')
def plot():
    from pandas_datareader import data
    import pandas as pd
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN # content delivery network

    import bokeh.io


    start = datetime.datetime(2018,10,1)
    end = datetime.datetime(2019,1,18)
    stock = "DIV"
    title_str = "Candlestick Chart for " + stock

    df = data.DataReader(name=stock, data_source="yahoo", start=start, end=end)


    # make a status column
    def inc_dec(c,o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value


    # create dimensions based on the changes and calculations
    df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close)/2
    df["Height"] = abs(df.Close - df.Open)

    bokeh.io.reset_output()

    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode = "scale_width")
    p.title.text = title_str
    p.grid.grid_line_alpha=0.3

    hours_12 = 12 * 60 * 60 * 1000


    # x value of highest point and lowest point of line segments
    p.segment(df.index, df.High, df.index, df.Low, color = "Black")

    # need to build out the individual candlesticks
    # passing dimensions of rectangle

    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
           hours_12, df.Height[df.Status == "Increase"], fill_color="#009966", line_color="black")

    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
           hours_12, df.Height[df.Status == "Decrease"], fill_color="#FF3333", line_color="black")



    # generates the source codein a tuple
    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_css=cdn_css,
    cdn_js=cdn_js)



if __name__=="__main__":
    app.run(debug=True)
